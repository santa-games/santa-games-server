from flask_httpauth import HTTPTokenAuth
from flask_sqlalchemy import SQLAlchemy

auth = HTTPTokenAuth(scheme='token')
db = SQLAlchemy()