from . import tic_tac_toe
from . import connect_4

game_types = { str(i) : game_type for (i, game_type) in enumerate((
    tic_tac_toe,
    connect_4,
))}

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