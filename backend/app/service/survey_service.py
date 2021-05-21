from flask import abort
from sqlalchemy import func, text, and_
from .auth_service import get_user_from_token, verify_token, create_token
from .user_service import get_user_by_id
from .team_service import get_team_by_id
from app.model.survey import Survey
from app.model.survey_options import Survey_Options
from app import bcrypt, db


def add_survey(team_id: int, creator_id: int, question: str):
    # while Survey.query.filter_by(question=question).first() is not None:
    #    abort(400, "Error creating survey: Question already exists for that team")
    survey = Survey(question=question, creator_id=creator_id)
    db.session.add(survey)
    db.session.commit()
    try:
        add_survey_to_team(survey, get_team_by_id(team_id))
    except:
        # db.session.rollback()
        abort(400, "Error with insert: Team member into created team")

    response_object = {
        'status': 'success',
        'message': 'Successfully created'
    }
    return response_object, 201


def add_survey_to_team(survey, team):
    connection = db.engine.connect()
    conn = connection.begin()
    statement = text(f"CALL new_survey({survey.survey_id}, {team.team_id});")
    try:
        connection.execute(statement)
        conn.commit()
    except Exception as e:
        print(f"Following error executing add_survey_to_team() from survery_service.py: {e}")
        # abort(400, 'Error with insert: Member')
    response_object = {
        'status': 'success',
        'message': 'Successfully added Survey to team'
    }
    return response_object, 201


def add_survey_option(surveys: dict, creator_id: int):  # {survey_id : option}
    for survey_id, option in surveys.items():
        if Survey_Options.query.filter_by(survey_id=survey_id, some_option=option).first() is None:
            survey_option = Survey_Options(survey_id=survey_id, some_option=option, creator_id=creator_id)
            db.session.add(survey_option)
            db.session.commit()
        else:
            print("Survey Option already exists for the survey!")
            # abort(400, "Survey Option already exists for the survey!")
        vote_survey_option(survey_id, option, user_id=creator_id)
    response_object = {
        'status': 'success',
        'message': 'Successfully voted'
    }
    return response_object, 201


def vote_survey_option(survey_id: int, option: str, user_id: int):
    connection = db.engine.connect()
    conn = connection.begin()
    statement = text(f"CALL new_survey_vote({survey_id}, '{option}', {user_id});")
    try:
        connection.execute(statement)
        conn.commit()
    except Exception as e:
        print(f"Following error executing vote_survey_option() from survery_service.py: {e}")
        # abort(400, 'Error with insert: Member')
    response_object = {
        'status': 'success',
        'message': 'Successfully voted'
    }
    return response_object, 201
