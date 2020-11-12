import json, uuid, logging, datetime, random
from flask import request, g, abort
from flask_restful import Resource, marshal_with, fields
from endpoints import api
from extensions import db, auth
import models
from game_types import game_types, STATE_PROPOSED, STATE_ACTIVE, STATE_COMPLETE, STATE_FORFEIT, STATE_CANCELLED

logger = logging.getLogger(__name__)

games_get_fields = {
    "game_id" : fields.Integer(attribute="id"),
    "game_state_id" : fields.Integer(),
    "host_user_id" : fields.Integer(),
    "guest_user_id" : fields.Integer(default=None),
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
            game = models.Game(host_user_id=g.current_user.id, game_type_id=game_type_id, datetime_created=datetime.datetime.now(), game_state_id=0) 
            db.session.add(game)
            db.session.commit()
            return game, 201
        except Exception as e:
            logger.error(e)
            abort(500, e.message)

game_get_fields = {
    "game_id" : fields.Integer(attribute="id"),
    "game_state_id" : fields.Integer(),
    "host_user_id" : fields.Integer(),
    "guest_user_id" : fields.Integer(default=None),
    "next_user_id" : fields.Integer(default=None),
    "win_user_id" : fields.Integer(default=None),
    "data" : fields.String(),
}

class Game(Resource):
    @marshal_with(game_get_fields)
    def get(self, game_id=None):
        if game_id is None: abort(400, "Must provide a game_id")

        game = models.Game.query.filter_by(id=game_id).first()
        if game is None:
            return abort(400, f"The provided game_id [{game_id}] was not found in the database.")

        return game, 200

    @auth.login_required
    def put(self, game_id=None):
        if request.json is None: return abort(400, "No json payload provided.")
        game_state_id = request.json.get('game_state_id')
        if game_state_id is None: return abort(400, "Must provide a game_state_id.")
        if game_id is None: abort(400, "Must provide a game_id")

        game = models.Game.query.filter_by(id=game_id).first()
        if game is None: return abort(400, f"The provided game_id [{game_id}] was not found in the database.")

        if g.current_user.id == game.host_user_id and game.game_state_id == STATE_PROPOSED and game_state_id == STATE_CANCELLED:
                game.game_state_id = STATE_CANCELLED
                db.session.commit()
                return None, 201
        elif (g.current_user.id == game.host_user_id or g.current_user.id == game.guest_user_id) and game.game_state_id == STATE_ACTIVE and game_state_id == STATE_FORFEIT:
                game.game_state_id = STATE_FORFEIT # probably want to track who forfiet. penalise (loss of points?)
                db.session.commit()
                return None, 201
        elif g.current_user.id != game.host_user_id and game.game_state_id == STATE_PROPOSED and game_state_id == STATE_ACTIVE:
                game.game_state_id = STATE_ACTIVE
                game.guest_user_id = g.current_user.id
                game_type = game_types[game.game_type_id]
                game.data = game_type.create()
                game.host_goes_first = random.choice([True, False])
                game.next_user_id = game.host_user_id if game.host_goes_first else game.guest_user_id
                db.session.commit()
                return 201
        else:
            return abort(400, "The requested state change was not valid.")

class Turns(Resource):

    @auth.login_required
    def post(self, game_id=None):
        if request.json is None: return abort(400, "No json payload provided.")
        if game_id is None: abort(400, "Must provide a game_id")
        game = models.Game.query.filter_by(id=game_id).first()

        if game is None: return abort(400, f"The provided game_id [{game_id}] was not found in the database.")
        if game.game_state_id != STATE_ACTIVE: return abort(400, f"Game [{game_id}] is not currently active.")
        if game.next_user_id != g.current_user.id: return abort(401, "Its not your turn.")

        player_action = request.json.get('action')
        if player_action is None: return abort(400, "A player action must be provided.")

        if game.host_goes_first: player_id = 0 if game.next_user_id == game.host_user_id else 1
        else: player_id = 1 if game.next_user_id == game.host_user_id else 0

        game_type = game_types[game.game_type_id]
        data, next_player_id, win_player_id = game_type.turn(game.data, player_id, player_action)

        if data is not None: game.data = data

        if win_player_id is not None:
            game.game_state_id = STATE_COMPLETE
            game.next_user_id = None
            game.win_user_id = convert_player_id(game, win_player_id)
        else:
            game.next_user_id = convert_player_id(game, next_player_id)
        db.session.commit()

def convert_player_id(game, player_id):
    if game.host_goes_first: return game.host_user_id if player_id == 0 else game.guest_user_id
    else: return game.guest_user_id if player_id == 0 else game.host_user_id

api.add_resource(Games, "/games")
api.add_resource(Game, "/games/<int:game_id>")
api.add_resource(Turns, "/games/<int:game_id>/turns")
