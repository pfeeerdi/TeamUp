from flask import abort
from sqlalchemy import func, text
from .auth_service import get_user_from_token, verify_token, create_token
from .user_service import get_user_by_id
from app.model.team import Team
from app import bcrypt, db
import random
import string


# import dateutil.parser


def add_team(team_name: string, creator_id: int):
    share_code = create_sharecode()
    while Team.query.filter_by(share_code=share_code).first() is not None:
        share_code = create_sharecode()
    team = Team(team_name=team_name, creator_id=creator_id, share_code=share_code)
    db.session.add(team)
    db.session.commit()
    try:
        add_team_member(get_user_by_id(creator_id), team)
    except:
        # db.session.rollback()
        abort(400, "Error with insert: Team member into created team")

    response_object = {
        'status': 'success',
        'message': 'Successfully created'
    }
    return response_object, 201


def create_sharecode():
    res = ""
    for i in range(6):
        res += random.choice(string.ascii_letters)
    return res


def add_team_member(user, team):
    connection = db.engine.connect()
    conn = connection.begin()
    statement = text(f"CALL new_teammember({team.team_id}, {user.user_id});")
    try:
        connection.execute(statement)
        conn.commit()
    except Exception as e:
        print(e)
        # abort(400, 'Error with insert: Member')
    response_object = {
        'status': 'success',
        'message': 'Successfully followed'
    }
    return response_object, 201


def get_team_by_id(team_id: int):
    team = Team.query.filter_by(team_id=team_id).first()
    if not team:
        abort(404, 'Team Not Found')
    else:
        return team
