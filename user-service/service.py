# user-service/service.py

from flask import jsonify
from models import db, User

class UserService:
    
    @staticmethod
    def register_user(data):
        # Handle user registration
        if User.query.filter_by(username=data['username']).first():
            return jsonify({'message': 'User already exists'}), 400
        new_user = User(username=data['username'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201

    @staticmethod
    def get_user(user_id):
        # Get a user by ID for verification
        user = User.query.get(user_id)
        if user:
            return jsonify({'id': user.id, 'username': user.username}), 200
        return jsonify({'message': 'User not found'}), 404
