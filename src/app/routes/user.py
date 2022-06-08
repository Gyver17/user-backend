from flask import Blueprint, request, jsonify
from flask_expects_json import expects_json
from sqlalchemy.exc import IntegrityError
from app.models.user_model import User
from app.utils.db import db
from app.validation.user_validation import registerSchema, loginSchema, updateSchema

users = Blueprint("users", __name__)

@users.route('/signup', methods=['POST'])
@expects_json(registerSchema)
def register_user():
    name = request.json['name']
    lastName = request.json['lastName']
    email = request.json['email']
    phone = request.json['phone']
    password = request.json['password']
    try:
        new_user = User(
        name, lastName, email['body'], email['domain'], phone, password
    )
        # save the object into the database
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({ "name": name, "lastName": lastName })
    except IntegrityError:
        db.session.rollback()
        return jsonify({ "message": "duplicate" }), 500

@users.route('/signin', methods=['POST'])
@expects_json(loginSchema)
def login_user():
    email = request.json['email']
    password = request.json['password']
    user = User.query.filter(User.body_email == email['body']).first()

    if user is None:
        return jsonify({ "message": "not found" }), 403

    if user.password != password:
        return jsonify({ "message": "invalid" }), 403
    # save the object into the database
    # db.session.commit()
    return jsonify({ "id":user.id, "name": user.name, "lastName": user.last_name })

@users.route('/user', methods=['GET'])
def get_users():
    users = []
    for user in User.query.all():
        users.append({
            "id": user.id,
            "name": user.name,
            "lastName": user.last_name,
            "email": f"{user.body_email}@{user.domain_email}",
            "phone": user.phone
        })
    return jsonify(users)

@users.route('/user/<id>', methods=['PUT'])
@expects_json(updateSchema)
def update_user(id):
    user = User.query.get(id)
    if user == None:
        return jsonify({ "message": "not found" })

    user.name = request.json['name']
    user.last_name = request.json['lastName']
    email = request.json['email']
    user.body_email = email['body']
    user.domain_email = email['domain']
    user.phone = request.json['phone']

    db.session.commit()

    return jsonify({ "message": "success" })

@users.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if user == None:
        return jsonify({ "message": "not found" })

    db.session.delete(user)
    db.session.commit()

    return jsonify({ "message": "success" })

