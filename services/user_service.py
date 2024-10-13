


from flask import Blueprint, jsonify, request

from db import db
from models.users import User

api = Blueprint('users', __name__)

@api.route('/register', methods=['POST'])
def register():
    data = request.json
    new_user = User(name=data['name'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added successfully!"}), 201

@api.route('/get_users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "name": user.name, "email": user.email, "password": user.password} for user in users])
