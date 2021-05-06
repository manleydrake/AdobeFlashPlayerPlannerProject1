from flask_login import UserMixin
from . import db
import datetime

class User(UserMixin,db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    events = db.relationship('Events')

class Events(UserMixin, db.Model):
    __tablename__='events'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", backref=db.backref('user',uselist='false'))

    name = db.Column(db.String(1000))
    event_name = db.Column(db.String(1000))
    date_time = db.Column(db.DateTime(timezone=True))
    caption = db.Column(db.String(1000))
