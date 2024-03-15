from flask import current_app, url_for, json
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(300), unique=True)
    # Add other user details as needed

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(300))
    age_group = db.Column(db.String(50))
    skill_level = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Foreign key to associate Order with User

    # Define relationship between User and Order
    user = db.relationship('User', backref=db.backref('orders', lazy=True))