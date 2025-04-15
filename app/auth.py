from flask import Blueprint, request, jsonify
from app import db
from app.models import User
from pdb import set_trace as sstt

auth = Blueprint('auth', __name__)

@auth.route('/index', methods=['GET', 'POST'])
@auth.route('/', methods=['GET', 'POST'])
def index():
    print("IN INDEX -- request.method", request.method)
    print("DB: ", db)
    return "INDEX"

@auth.route('/register', methods=['POST'])
def register():
    print("")
    print("IN register - request.method:", request.method)

    data = request.get_json()
    print("IN register - data:", data)

    email = data.get('email')
    name = data.get('name')
    password = data.get('password')
    
    if not email or not name or not password:
        return jsonify({'error': 'Missing required fields'}), 400
        
    existing_user = User.query.filter_by(email=email).first()
    print("existing_user: ", existing_user)

    if existing_user:
        return jsonify({'error': 'User already exists'}), 400

    user = User(email=email, name=name)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@auth.route('/login', methods=['POST'])
def login():
    print("IN login - request.method:", request.method)

    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email:
        return jsonify({'error': 'Missing email'}), 400

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({'error': 'Invalid email or password'}), 400

    return jsonify({'message': 'Logged in successfully', 'user': user.id}), 200


@auth.route('/check_email', methods=['POST'])
def check_email():
    print("IN check_email - request.method:", request.method)

    data = request.get_json()
    email = data.get('email')
    
    if not email:
        return jsonify({'error': 'Missing email'}), 400

    user = User.query.filter_by(email=email).first()

    if user:
        return jsonify({'message': 'You already have an account'}), 200
    else:
        return jsonify({'message': 'Email does not exist - SignUp'}), 200


@auth.route('/signup', methods=['POST'])
def signup():
    print("")
    print("IN signup")
        
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    password = data.get('password')
    super_user_code = data.get('super_user_code')

    if super_user_code == 'wearethechampions':
        if email and name and password:
            if User.query.filter_by(email=email).first():
                return jsonify({'error': 'User already exists'}), 400

            user = User(email=email, name=name)
            user.set_password(password)
            db.session.add(user)
            sstt()
            db.session.commit()

            return jsonify({'message': 'User signed up successfully'}), 201
        else:
            return jsonify({'error': 'Missing required fields'}), 400
    else:
        return jsonify({'error': 'Invalid super user code'}), 403
