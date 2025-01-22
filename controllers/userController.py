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

def create_user(name,email):
    new_user = User(name, email)
    db.session.add(new_user)
    db.session.commit()
    return new_user.to_dict()
    return "hola"

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
