from flask import abort
from sqlalchemy import func, text
from .auth_service import get_user_from_token, verify_token, create_token
from app.model.user import User
from app.model.team import Team
from app import bcrypt, db
#import dateutil.parser


def get_user_by_id(user_id: int):
    user = User.query.filter_by(user_id=user_id).first()
    if not user:
        abort(404, 'User Not Found')
    else:
        return user


def get_all_usernames():
    users = User.query.with_entities(User.username).all()
    user_list = []
    for a in users:
        for b in a:
            user_list.append(b)
    return user_list


def get_all_users():
    users = User.query.all()
    return users


def get_user_by_username(username):
    user = User.query.filter(func.lower(User.username) == func.lower(username)).first()
    if user == None:
        abort(400, 'User not found')
    return user


def get_user_by_email(email):
    user = User.query.filter_by(email=email).first()
    if user == None:
        abort(400, 'User not found')
    return user


def register(username, email, lastName, firstName, password):
    if User.query.filter_by(username=username).first() != None or User.query.filter_by(email=email).first() != None:
        abort(400, 'User already exist')

    hashed_password = bcrypt.generate_password_hash(password, 10)
    user = User(username=username, email=email, lastName=lastName, firstName=firstName,
                password=hashed_password)
    db.session.add(user)
    db.session.commit()

    response_object = {
        'status': 'success',
        'message': 'Successfully created'
    }
    return response_object, 201

def login(email, password):
    user = get_user_by_email(email)
    password_matched_email = user.password
    if not bcrypt.check_password_hash(password_matched_email, password):
        abort(400, 'Wrong credentials')
    token = create_token(email)
    return token, user.username

def get_teams_by_username(username):
    teams = None

