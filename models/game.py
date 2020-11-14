from extensions import db

class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    datetime_created = db.Column(db.DateTime, nullable=False)
    host_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    guest_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True, default=None)
    game_type_id = db.Column(db.String, nullable=False)
    host_goes_first = db.Column(db.Boolean)
    game_state_id = db.Column(db.Integer)
    next_user_id = db.Column(db.Integer)
    win_user_id = db.Column(db.Integer)
    number_of_turns = db.Column(db.Integer, nullable=False, default=0)
    next_turn_expiry = db.Column(db.DateTime)
    data = db.Column(db.String)