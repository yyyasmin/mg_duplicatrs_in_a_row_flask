from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'  # Use plural form to avoid reserved keyword conflict

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    email = db.Column(db.String(500), unique=True, nullable=False)
    password_hash = db.Column(db.String(500), nullable=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Order(db.Model):
    __tablename__ = 'orders'  # Use plural form to avoid reserved keyword conflict

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    age_group_id = db.Column(db.Integer, db.ForeignKey('age_groups.id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))
    skill_level_id = db.Column(db.Integer, db.ForeignKey('skill_levels.id'))

class Subject(db.Model):
    __tablename__ = 'subjects'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
  
class AgeGroup(db.Model):
    __tablename__ = 'age_groups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
  
class SkillLevel(db.Model):
    __tablename__ = 'skill_levels'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(1000))

class RelationshipLevel(db.Model):
    __tablename__ = 'relationship_levels'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    description = db.Column(db.String(1000))
    
class MatchingType(db.Model):
    __tablename__ = 'matching_types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    description = db.Column(db.String(1000))
     
class Interest(db.Model):
    __tablename__ = 'interests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    description = db.Column(db.String(1000))
      
class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    description = db.Column(db.String(1000))
    
class PartnerProfile(db.Model):
    __tablename__ = 'partner_profiles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    gender = db.Column(db.String(10))
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))
    age_group_id = db.Column(db.Integer, db.ForeignKey('age_groups.id'))
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    relationship_level_id = db.Column(db.Integer, db.ForeignKey('relationship_levels.id'))
    matching_type_id = db.Column(db.Integer, db.ForeignKey('matching_types.id'))
    playmate_email = db.Column(db.String(500))
    date = db.Column(db.Date)
    time = db.Column(db.Time)
