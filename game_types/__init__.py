from . import tic_tac_toe

game_types = {
    "tic_tac_toe": tic_tac_toe.TicTacToe()
}

STATE_PROPOSED = 0
STATE_ACTIVE = 1
STATE_COMPLETE = 2

STATES = [
    STATE_PROPOSED,
    STATE_ACTIVE,
    STATE_COMPLETE,
]