from extensions import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, unique=True, nullable=False)
    datetime_created = db.Column(db.DateTime, nullable=False)
    token = db.Column(db.String, unique=True, nullable=False)
    games_won = db.Column(db.Integer, nullable=False, default=0)
    games_lost = db.Column(db.Integer, nullable=False, default=0)
