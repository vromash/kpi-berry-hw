from flask_restful import Api
from config import app

from api.reading import ReadingApi
from api.readings_list import ReadingListApi
from api.statistics import ReadingStatisticsApi

api = Api(app)

api.add_resource(ReadingApi, '/reading', '/reading/', '/reading/<int:id>')
api.add_resource(ReadingListApi, '/all-readings', '/all-readings/')
api.add_resource(ReadingStatisticsApi, '/statistics', '/statistics/')