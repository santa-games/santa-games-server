import json, uuid, logging, datetime
from flask import request, g, abort
from flask_restful import Resource, marshal_with, fields
from endpoints import api
from extensions import db, auth
import models

logger = logging.getLogger(__name__)

users_fields = {
    "user_id" : fields.Integer(attribute="id"),
    "user_name" : fields.String,
}

user_register_fields = {
    "user_id" : fields.Integer(attribute="id"),
    "user_name" : fields.String,
    "token" : fields.String,
}

user_fields = {
    "user_id" : fields.Integer(attribute="id"),
    "user_name" : fields.String,
}

class Users(Resource):
    @marshal_with(users_fields)
    def get(self):
        try:
            users = models.User.query.all()
            return users, 200
        except Exception as e:
            abort(500, str(e))

    @marshal_with(user_register_fields)
    def post(self):
        user_name = request.json.get('user_name')
        if user_name is None: abort(400, "No [user_name] provided.")
        if models.User.query.filter_by(user_name=user_name).count() > 0: abort(400, "[user_name] already exists.")
        try:
            user = models.User(user_name=user_name, token=str(uuid.uuid4()), datetime_created=datetime.datetime.now()) 
            db.session.add(user)
            db.session.commit()
            return user, 201
        except Exception as e:
            logger.error(e)
            abort(500)

    @auth.login_required
    def delete(self):
        db.session.delete(g.current_user)

class User(Resource):
    @marshal_with(user_fields)
    def get(self, user_id=None):
        if user_id is None: abort(400, "Must provide a user id")
        user = models.User.query.filter_by(id=user_id).first()
        if user is None: abort(400, "No user found with that id.")
        return user, 200

api.add_resource(Users, "/users")
api.add_resource(User, "/users/<int:user_id>")