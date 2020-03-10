from flask_restful import Resource
from flask_sqlalchemy import sqlalchemy
from model import readings_schema, Reading

class ReadingListApi(Resource):
    def get(self):
        try:
            all_readings = Reading.query.all()
            return readings_schema.dump(all_readings), 200
        except sqlalchemy.exc.OperationalError:
            return 'Database is configured wrong!', 500
        except:
            return 'The requested URL was not found on the server.', 404