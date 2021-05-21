from flask import Blueprint
from flask_restx import Api
from .user import api as user_ns
#from .team import api as team_ns


blueprint = Blueprint("api", __name__)

api = Api(
    blueprint, title="FLASK RESTX API", version="1.0", description="FLASK RESTX API "
)

api.add_namespace(user_ns, path='/user')
#api.add_namespace(team_ns, path='/team')

