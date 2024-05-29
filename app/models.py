from flask import current_app, url_for, json
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(300), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)  # For authentication
    
    orders = db.relationship('Order', backref='user', lazy=True)
    partner_profiles = db.relationship('PartnerProfile', backref='user', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(300))
    age_group = db.Column(db.String(50))
    skill_level = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class PartnerProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    interest = db.Column(db.String(300))
    friendship_level = db.Column(db.String(50))
    location = db.Column(db.String(300))
    date = db.Column(db.String(50))
    time = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
