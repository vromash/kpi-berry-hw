from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
from config import app

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Reading(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    value = db.Column(db.Float, nullable=False)
    datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Reading %r>' % seld.id

class ReadingSchema(ma.Schema):
    class Meta:
        fields = ('id', 'value', 'datetime')

reading_schema = ReadingSchema()
readings_schema = ReadingSchema(many=True)
