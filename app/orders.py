from flask import request, jsonify
from . import db
from .models import User, Order, PartnerProfile
from flask import Blueprint

ord = Blueprint('ord', __name__, template_folder='templates')

@ord.route('/', methods=['GET', 'POST'])
@ord.route('/index', methods=['GET', 'POST'])
def index():
    return " \n IN index"

@ord.route('/submit_order', methods=['POST'])
def submit_order():
    data = request.get_json()
    print("data: ", data)

    email = data.get('email')
    password = data.get('password')  # Add password field in the request
    
    # Check if the user already exists
    user = User.query.filter_by(email=email).first()

    if not user:
        user = User(email=email)
        user.set_password(password)  # Set the password hash
        db.session.add(user)
        db.session.commit()

    # Extract order details from the request
    subject = data.get('subject')
    age_group = data.get('ageGroup')
    skill_level = data.get('skillLevel')

    # Create a new order associated with the user
    order = Order(subject=subject, age_group=age_group, skill_level=skill_level, user=user)
    db.session.add(order)
    
    # Extract partner profile details from the request
    name = data.get('name')
    age = data.get('age')
    gender = data.get('gender')
    interest = data.get('interest')
    friendship_level = data.get('friendshipLevel')
    location = data.get('location')
    date = data.get('date')
    time = data.get('time')

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
        user=user
    )
    db.session.add(partner_profile)
    db.session.commit()
    
    response_data = {'message': 'Order and partner profile submitted successfully!'}
    return jsonify(response_data)
