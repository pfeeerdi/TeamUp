from flask_restx import Namespace, fields

class UserDto():
    api = Namespace('users', description='user related operations')
    model = api.model('user', {
        'id': fields.Integer(readonly=True, attribute='user_id'),
        'username': fields.String(required=True),
        'email': fields.String(required=True),
        'lastName': fields.String(required=True),
        'firstName': fields.String(required=True),
        'join_date': fields.DateTime(readonly=True),
        'team_ids': fields.List(
            fields.Integer(attribute='team_id'),
            attribute='teams'
        ),
        'voted_surveys': fields.Integer(
            attribute=lambda x: len(x.survey_votes)
        )
    })

    model_profile = api.model('profile', {
        'id': fields.Integer(readonly=True, attribute='user_id'),
        'username': fields.String(required=True),
        'email': fields.String(required=True),
        'lastName': fields.String(required=True),
        'firstName': fields.String(required=True),
        'join_date': fields.DateTime(readonly=True),
        'teams': fields.Integer(attribute=lambda x: len(x.teams))
    })
    model_update_send = api.model('update', {
        'lastName': fields.String(required=True),
        'firstName': fields.String(required=True),
    })
    model_update_receive = api.model('update', {
        'lastName': fields.String(required=True),
        'firstName': fields.String(required=True),
    })
    model_username = api.model('username', {
        'username': fields.String(required=True)
    })
    model_login = api.model('login', {
        'email': fields.String(required=True),
        'password': fields.String(required=True)
    })
    model_token = api.model('token', {
        'token': fields.String(required=True)
    })
    model_signup = api.model('signup', {
        'username': fields.String(required=True),
        'email': fields.String(required=True),
        'lastName': fields.String(required=True),
        'firstName': fields.String(required=True),
        'password': fields.String() # not to good idea
    })
