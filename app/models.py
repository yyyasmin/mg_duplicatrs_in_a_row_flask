from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    email = db.Column(db.String(500), unique=True, nullable=False)
    password_hash = db.Column(db.String(500), nullable=False)

    orders = db.relationship('Order', backref='user', lazy=True)
    partner_profiles = db.relationship('PartnerProfile', backref='user', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    subject = db.Column(db.String(500))
    age_group = db.Column(db.String(50))
    skill_level = db.Column(db.String(50))

class PartnerProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
        
    email = db.Column(db.String(500))
    age = db.Column(db.String(10))
    gender = db.Column(db.String(10))
    interest = db.Column(db.String(500))
    relationship_level = db.Column(db.String(300))
    location = db.Column(db.String(300))
    date = db.Column(db.String(20))
    time = db.Column(db.String(10))
    matching_type = db.Column(db.String(20))
