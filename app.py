import logging, os, json, logging, math, urllib, uuid, datetime, random
from flask import Flask, escape, jsonify, request, abort, g
from flask_cors import CORS
from models import User
from extensions import db, auth
from endpoints import api_blueprint

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("santa-games")
logger.info("Welcome to Santa-Games")

DB_CONNECTION = os.environ.get("SANTA_GAMES_SQLALCHEMY_DATABASE_URI")

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONNECTION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(api_blueprint)

@auth.verify_token
def verify_token(token):
    if token is None: return False
    g.current_user = User.query.filter_by(token=token).first()
    is_verified = g.current_user is not None
    if is_verified: logger.info(f"AUTHORISED: [{token}]")
    else: logger.info(f"DENIED: [{token}]")
    return is_verified

@auth.error_handler
def auth_error():
    return abort(401, "Access Denied.")

@app.route("/")
def index():
    return "I think the API is running? ¯\\_(ツ)_/¯"

@app.route("/shutdown")
def shutdown():
    request.environ.get('werkzeug.server.shutdown')()

if __name__ == "__main__":
    app.run(port="80",debug=False)