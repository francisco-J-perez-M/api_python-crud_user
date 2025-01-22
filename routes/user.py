from flask import Blueprint, jsonify, request
from controllers.userController import (
    get_all_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user
)

user_bp = Blueprint('users', __name__)

@user_bp.route('/', methods=['GET'])
def index():
    users = get_all_users()
    return jsonify(users)

@user_bp.route('/<int:user_id>', methods=['GET'])
def show(user_id):
    user = get_user_by_id(user_id)
    return jsonify(user)

@user_bp.route('/', methods=['POST'])
def store():
    data = request.get_json()
    result = create_user(data)
    return jsonify(result)

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update(user_id):
    data = request.get_json()
    result = update_user(user_id, data)
    return jsonify(result)

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def destroy(user_id):
    result = delete_user(user_id)
    return jsonify(result)
