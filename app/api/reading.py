from flask_restful import Resource, reqparse
from flask_sqlalchemy import sqlalchemy
from model import db, reading_schema, Reading

parser = reqparse.RequestParser()
parser.add_argument('value')

class ReadingApi(Resource):
    def get(self, id):
        try:
            reading = Reading.query.get_or_404(id)
            return reading_schema.dump(reading), 200
        except sqlalchemy.exc.OperationalError:
            return 'Database is configured wrong!', 500
        except:
            return 'The requested URL was not found on the server.', 404

    def post(self):        
        params = parser.parse_args()
        try:
            new_reading = Reading(value = params['value'])
            db.session.add(new_reading)
            db.session.commit()
            return reading_schema.dump(new_reading), 201
        except sqlalchemy.exc.OperationalError:
            return 'Database is configured wrong!', 500
        except:
            return 'The requested URL was not found on the server.', 404

    def put(self, id):
        params = parser.parse_args()
        
        try:
            reading_to_update = Reading.query.get_or_404(id)
            reading_to_update.value = params['value']
            db.session.commit()
            return reading_schema.dump(reading_to_update), 201
        except sqlalchemy.exc.OperationalError:
            return 'Database is configured wrong!', 500
        except:
            return 'The requested URL was not found on the server.', 404

    def delete(self, id):
        try:
            reading_to_delete = Reading.query.get_or_404(id)
            db.session.delete(reading_to_delete)
            db.session.commit()
            return '', 204
        except sqlalchemy.exc.OperationalError:
            return 'Database is configured wrong!', 500
        except:
            return 'The requested URL was not found on the server.', 404