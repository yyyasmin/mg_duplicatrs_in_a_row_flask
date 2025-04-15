from flask import Blueprint, jsonify, request
from app import db
from app.models import User, Order, PartnerProfile, Subject, AgeGroup, SkillLevel, Location, RelationshipLevel, MatchingType
from pprint import pprint
from datetime import datetime
from pdb import set_trace as sstt

ord = Blueprint('ord', __name__)

### HELPERS ###

def add_value_to_class(class_name, value):
    print("\nIN add_value_to_class")
    print(f"class_name: {class_name} --- value: {value}")

    ModelClass = globals()[class_name]
    obj = ModelClass.query.filter(ModelClass.name == value).first()
    if not obj:
        obj = ModelClass(name=value)
        db.session.add(obj)
        db.session.commit()
    obj = ModelClass.query.filter(ModelClass.name == value).first()
    print(f"{class_name}: {obj.name} added to DB")
    return obj

@ord.route('/get_user', methods=['POST'])
def get_user(name, email):
    print("\nIN get_user")
    print(f"LOOKING FOR USER WITH NAME: {name} and EMAIL: {email}")

    user = None
    if email and name:
        user = User.query.filter_by(email=email, name=name).first()
        if not user:
            print(f"NO USER WITH NAME: {name} and EMAIL: {email}")
            return -1
    elif email:
        user = User.query.filter_by(email=email).first()
        if not user:
            print(f"NO USER WITH EMAIL: {email}")
            return -1
    elif name:
        user = User.query.filter_by(name=name).first()
        if not user:
            print(f"NO USER WITH NAME: {name}")
            return -1
    print("USER:", user)
    return user
    '''
    # THIS should be put in the caller
    if user:
        return jsonify({'user': {'name': user.name, 'email': user.email}})
    return jsonify({'error': 'User not found'}), 404
    '''

@ord.route('/get_or_create_user', methods=['POST'])
def get_or_create_user(name, email):
    print("")
    print("IN get_or_create_user")

    #password = data.get('password', 'defaultpassword')
    password = 'no_paswword'
    print("\nIN get_or_create_user")
    print(f"LOOKING FOR USER WITH NAME: {name} and EMAIL: {email}")
    
    if email and name:
        user = User.query.filter_by(email=email, name=name).first()
        if not user:
            print(f"NO USER WITH NAME: {name} and EMAIL: {email} - CREATING NEW USER")
            user = User(name=name, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            print(f"USER {user.name} , {user.email} has created")
        return user
        
    if email:
        user = User.query.filter_by(email=email).first()
        if not user:
            print(f"NO USER WITH EMAIL: {email} - CREATING NEW USER")
            user = User(email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
        return user
        
    if name:
        user = User.query.filter_by(name=name).first()
        if not user:
            print(f"NO USER WITH NAME: {name}")
            return -1
        return user
    return -1

@ord.route('/submit_order', methods=['POST'])
def submit_order():
    print("\nIN submit_order")

    data = request.get_json()
    pprint(data)

    user = get_or_create_user(name='', email=data.get('email'))
    if user == -1:
        return jsonify({'error': 'User not found or created'}), 400

    age_group_id = add_value_to_class('AgeGroup', data.get('ageGroup')).id
    subject_id = add_value_to_class('Subject', data.get('subject')).id
    skill_level_id = add_value_to_class('SkillLevel', data.get('skillLevel')).id
    
    sstt()
    
    order = Order(user_id=user.id,
                  age_group_id=age_group_id,
                  subject_id=subject_id,
                  skill_level_id=skill_level_id)
    db.session.add(order)
    db.session.commit()
    print(f"ORDER {order} has been created")

    response_data = {'message': 'Order submitted successfully!'}
    return jsonify(response_data)

@ord.route('/submit_partner_profile', methods=['POST'])
def submit_partner_profile():
    data = request.get_json()
    print("\nIN submit_partner_profile")
    pprint(data)

    user = get_or_create_user(name='', email=data.get('userEmail'))
    if user == -1:
        return jsonify({'error': 'User not found or created'}), 400

    gender = data.get('gender')
    subject_id = add_value_to_class('Subject', data.get('subject')).id
    age_group_id = add_value_to_class('AgeGroup', data.get('ageGroup')).id
    location_id = add_value_to_class('Location', data.get('location')).id
    relationship_level_id = add_value_to_class('RelationshipLevel', data.get('relationshipLevel')).id
    matching_type_id = add_value_to_class('MatchingType', data.get('matchingType')).id
    playmate_email = data.get('playmateEmail')

    playing_date_str = data.get('playingDate')
    playing_date_obj = datetime.fromisoformat(playing_date_str.replace('Z', '+00:00'))
    date = playing_date_obj.date()
    time = playing_date_obj.time()

    partner_profile = PartnerProfile(
        user_id=user.id,
        gender=gender,
        subject_id=subject_id,
        age_group_id=age_group_id,
        location_id=location_id,
        relationship_level_id=relationship_level_id,
        matching_type_id=matching_type_id,
        playmate_email=playmate_email,
        date=date,
        time=time
    )

    db.session.add(partner_profile)
    db.session.commit()
    print(f"PartnerProfile {partner_profile} has been created")

    response_data = {'message': 'Partner profile submitted successfully!'}
    return jsonify(response_data)
