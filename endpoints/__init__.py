from flask import Blueprint
from flask_restful import Api
from exceptions import errors

api_blueprint = Blueprint("api", __name__, url_prefix='/api')
api = Api(api_blueprint, errors=errors)

from . import users
from . import games