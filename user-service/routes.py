from flask import Blueprint, request, jsonify
from models import db, User
from service import UserService

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    new_user = User(username=data['username'])

@user_routes.route('/get<int:user_id>', methods={'GET'})
def get_user(user_id):
    user = user.query.get() 
    return UserService.get_user(user_id)