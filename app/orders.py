from flask import request, jsonify
from . import db  # Import db from the package (__init__.py)
from .models import User, Order

from flask import Blueprint
ord = Blueprint(
    'ord', __name__,
    template_folder='templates'
)
 
@ord.route('/', methods=['GET', 'POST'])
@ord.route('/index', methods=['GET', 'POST'])
def index():
    return(" \n IN index")
    
    
@ord.route('/submit_order', methods=['POST'])
def submit_order():
    # Assuming you receive data in JSON format
    data = request.get_json()
    print("data: ", data)

    # Extract user details from the request
    email = data.get('email')

    # Check if the user already exists
    user = User.query.filter_by(email=email).first()

    # If the user doesn't exist, create a new user
    if not user:
        user = User(email=email)
        db.session.add(user)
        db.session.commit()

    # Extract order details from the request
    subject = data.get('subject')
    age_group = data.get('ageGroup')  # Adjust the key to match frontend data
    skill_level = data.get('skillLevel')  # Adjust the key to match frontend data

    # Create a new order associated with the user
    order = Order(subject=subject, age_group=age_group, skill_level=skill_level, user=user)
    db.session.add(order)
    db.session.commit()
        
    response_data = {'message': 'Order submitted successfully!'}
    return jsonify(response_data)
