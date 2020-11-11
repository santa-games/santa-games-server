from extensions import db

class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    datetime_created = db.Column(db.DateTime, nullable=False)
    host_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    guest_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    game_type_id = db.Column(db.Integer, nullable=False)
    game_state = db.Column(db.Integer) # e.g. challenge etc.
    next_turn_player = db.Column(db.Integer)  # 0 or 1 for which player goes next
    next_turn_expiry = db.Column(db.DateTime) # when the game is automatically forfiet
    data = db.Column(db.String)


# want to post a game. e.g
# 
# post 
# {
#   game_type: 0,
# }

# how to accept games

