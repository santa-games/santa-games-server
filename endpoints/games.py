import json, uuid, logging, datetime
from flask import request, g, abort
from flask_restful import Resource, marshal_with, fields
from endpoints import api
from extensions import db, auth
import models
from game_types import game_types

logger = logging.getLogger(__name__)

games_get_fields = {
    "game_id" : fields.Integer(attribute="id"),
}

games_post_fields = {
    "game_id" : fields.Integer(attribute="id"),
}

class Games(Resource):
    @marshal_with(games_get_fields)
    def get(self):
        try:
            games = models.Game.query.all()
            return games, 200
        except Exception as e:
            abort(500, str(e))

    @auth.login_required
    @marshal_with(games_post_fields)
    def post(self):

        game_type_id = request.json.get('game_type_id')
        if game_type_id is None: abort(400, "No [game_type_id] provided.")

        if game_type_id not in game_types.keys(): abort(400, f"[game_type_id] of [{game_type_id}] not a supported game.")

        try:
            game = models.Game(host_user_id=g.current_user.id, game_type_id=game_type_id, datetime_created=datetime.datetime.now(), game_state=0) 
            db.session.add(game)
            db.session.commit()
            return game, 201
        except Exception as e:
            logger.error(e)
            abort(500)

api.add_resource(Games, "/games")