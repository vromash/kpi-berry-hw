from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import sqlalchemy
from model import db, reading_schema, readings_schema, Reading

from scipy import mean
from scipy.stats import shapiro, sem, t
from statsmodels.tsa.stattools import adfuller
import numpy as np

parser = reqparse.RequestParser()
parser.add_argument('from')
parser.add_argument('to')

class ReadingStatisticsApi(Resource):
    readings_values = []

    def get(self):
        return self.retrieve_stats()

    def retrieve_stats(self):
        try:
            self.get_values()

            count = len(self.readings_values)
            average = mean(self.readings_values)
            variance = np.var(self.readings_values)

            stats = {
                "count": count, 
                "mean": average,
                "variance": variance
            }        

            if self.is_gaussian():
                start, end = self.get_confidence_interval(count, average)
                stats["normal_dist"] = True
                stats["confidence_interval_start"] = start
                stats["confidence_interval_end"] = end
            else:
                stats["normal_dist"] = False

            stats["stationary"] = self.is_stationary()
            return stats, 200
        except ValueError:
            return 'Provided data is not enough data for providing statistics. Try different time window.', 500
        except sqlalchemy.exc.ArgumentError:
            return 'Wrong time window.', 400

    def get_values(self):
        params = parser.parse_args()

        all_readings = Reading.query.\
            filter(Reading.datetime >= params['from']).\
            filter(Reading.datetime <= params['to'])

        all_readings = readings_schema.dump(all_readings)
        self.readings_values = [r.get("value") for r in all_readings]        
        
    def is_gaussian(self):
        stat, p = shapiro(self.readings_values)
        return True if p > 0.05 else False

    def get_confidence_interval(self, count, avr):
        confidence = 0.95
        std_err = sem(self.readings_values)
        h = std_err * t.ppf((1 + confidence) / 2, count - 1)
        start = avr - h
        end = avr + h

        return start, end

    def is_stationary(self):
        result = adfuller(self.readings_values)
        return True if result[0] < result[4]['5%'] else False
