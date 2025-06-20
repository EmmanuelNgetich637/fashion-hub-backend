from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.user import User
from app.schemas.user_schema import user_schema
from app.utils.security import hash_password
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register',methods=['POST'])
def register():
    data = request.get_json()

    #Validate input using Marshmallow
    errors = user_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    
    #Check for existing user
    if User.query.filter((User.username == data['username']) | (User.email == data['email'])).first():
        return jsonify({"error": "Username or email already exists"}), 400

    #Hash password
    hashed_pw = hash_password(data['password'])

    # Create user
    user = User(
        username=data['username'],
        email=data['email'],
        password_hash=hashed_pw
    )

    db.session.add(user)
    db.session.commit()

     # Generate token
    access_token = create_access_token(identity=user.id)

    return jsonify({
        "message": "User registered successfully!",
        "token": access_token,
        "user": user_schema.dump(user)
    }), 201