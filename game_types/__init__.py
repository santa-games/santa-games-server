from . import tic_tac_toe

game_types = {
    "tictactoe": tic_tac_toe
}

STATE_PROPOSED = 0
STATE_ACTIVE = 1
STATE_COMPLETE = 2
STATE_FORFEIT = 3
STATE_CANCELLED = 4

STATES = [
    STATE_PROPOSED,
    STATE_ACTIVE,
    STATE_COMPLETE,
    STATE_FORFEIT,
    STATE_CANCELLED,
]