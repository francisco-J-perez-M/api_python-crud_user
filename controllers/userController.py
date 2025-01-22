from models.User import User
from config import db

def get_all_users():
    users = User.query.all()
    return [user.to_dict() for user in users]

def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found"}, 404
    return user.to_dict()

def create_user(data):
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return {"error": "Name and email are required"}, 400

    if User.query.filter_by(email=email).first():
        return {"error": "Email already exists"}, 400

    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()

    return new_user.to_dict(), 201

def update_user(user_id, data):
    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found"}, 404

    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)

    db.session.commit()
    return user.to_dict()

def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found"}, 404

    db.session.delete(user)
    db.session.commit()
    return {"message": "User deleted successfully"}
