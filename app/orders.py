from flask import request
from app import app, db
from app.models import User, Order

# Modify your Flask route or view function to handle user input and save it to the database
@app.route('/submit_order', methods=['POST'])
def submit_order():
    # Assuming you receive data in JSON format
    data = request.get_json()

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
    age_group = data.get('age_group')
    skill_level = data.get('skill_level')

    # Create a new order associated with the user
    order = Order(subject=subject, age_group=age_group, skill_level=skill_level, user=user)
    db.session.add(order)
    db.session.commit()

    return 'Order submitted successfully!'
