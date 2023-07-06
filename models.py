from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
'''
    Author: Anthoniraj Amalanathan
    Date: Last Modified: 05-Jul-2023
    Description: ALL Database Models for ORM 
'''

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password =  db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile = db.Column(db.String(15), nullable=False)
  
    def __repr__(self):
        return '<User %r>' % self.username

class UserActivity(db.Model):
    __tablename__ = "user_activity"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    activity =  db.Column(db.String(120), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    ipaddress = db.Column(db.String(50), nullable=False)
 
    def __init__(self, user_id, activity, ipaddress):
        self.user_id = user_id
        self.activity = activity
        self.ipaddress = ipaddress