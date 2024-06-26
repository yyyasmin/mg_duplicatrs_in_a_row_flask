from flask import Blueprint, jsonify, request
from app import db
from app.models import User, Order, PartnerProfile
from pdb import set_trace as sstt

ord = Blueprint('ord', __name__)

@ord.route('/submit_order', methods=['POST'])
def submit_order():
    print("")
    print("IN submit_order")
    data = request.get_json()
    print("data: ", data)
    
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')  # Add password field in the request
    
    sstt()

    if not password:
        password = 'userWithNoPassword'
    
    # Check if the user already exists
    user = User.query.filter_by(email=email).first()

    if not user:
        user = User(name=name, email=email)
        user.set_password(password)  # Set the password hash
        db.session.add(user)
        db.session.commit()

    # Extract order details from the request
    subject = data.get('subject')
    age_group = data.get('ageGroup')
    skill_level = data.get('skillLevel')
    
    print("")
    print("SUBJECT: ", subject)
    print("age_group: ", age_group)
    print("skill_level: ", skill_level)

    # Create a new order associated with the user
    order = Order(subject=subject, age_group=age_group, skill_level=skill_level, user=user)
    db.session.add(order)
    db.session.commit()
    
    response_data = {'message': 'Order submitted successfully!'}
    return jsonify(response_data)

@ord.route('/submit_partner_profile', methods=['POST'])
def submit_partner_profile():
    data = request.get_json()
    print("")
    print("IN submit_partner_profile")
    print("DB:", db)
    print("data: ", data)

    email = data.get('email')
    # Retrieve the user based on email
    user = User.query.filter_by(email=email).first()
    
    print("USER: ", user)
    sstt()

    if not user:
        return jsonify({'error': 'User not found!'})

    # Extract partner profile details from the request
    name = data.get('partnerName')
    age = data.get('age')
    gender = data.get('gender')
    interest = data.get('interest')
    friendship_level = data.get('friendshipLevel')
    location = data.get('location')
    date = data.get('date')
    time = data.get('time')
    matching_type = data.get('matchingType')  # Add matching type field

    # Create a new partner profile associated with the user
    partner_profile = PartnerProfile(
        name=name,
        age=age,
        gender=gender,
        interest=interest,
        friendship_level=friendship_level,
        location=location,
        date=date,
        time=time,
        matching_type=matching_type,  # Include matching type in the creation
        user=user
    )
    db.session.add(partner_profile)
    db.session.commit()
    
    response_data = {'message': 'Partner profile submitted successfully!'}
    return jsonify(response_data)
    
    
@ord.route('/submit_user_details', methods=['POST'])
def submit_user_details():
    data = request.get_json()
    print("data: ", data)

    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    if not email or not name or not phone:
        return jsonify({'error': 'Missing required fields'}), 400

    # Check if the user already exists
    user = User.query.filter_by(email=email).first()

    if not user:
        user = User(email=email, name=name)
        db.session.add(user)
        db.session.commit()

    response_data = {'message': 'User details submitted successfully!'}
    return jsonify(response_data)
    
