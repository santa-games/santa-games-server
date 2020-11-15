import logging

logger = logging.getLogger("santa-games.game_types.connect_4")

name = "connect 4"
width = 7
height = 6
connect_length = 4

def create():
    return " " * width * height

def turn(game_data, player_id, player_action):
    # check the move is valid
    x = int(player_action) if player_action.isdigit() else None
    if x is None:
        logger.debug(f"Invalid player_action of [{player_action}], Must be an integer.")
        return None, None, None 
    
    if x < 0 or x >= width:
        logger.debug(f"Invalid player_action of [{player_action}], must be an integer greater than zero, or less than {width}.")
        return None, None, None

    index = get_index(x, 0)
    if game_data[index] != ' ':
        logger.debug(f"Invalid player_action of [{player_action}], the space chosen was taken.")
        return None, None, None

    # set the next game state
    found_index = None
    for y in range(height-1, -1, -1):
        test_index = get_index(x, y)
        if game_data[test_index] != ' ':
            continue
        found_index = test_index
        break
    if found_index is None:
        logger.debug(f"Found index wasn't free. Did something go wrong?")
        return None, None, None
    player_symbol = get_player_symbol(player_id)
    next_game_data = game_data[:found_index] + player_symbol + game_data[found_index+1:]

    # work out the next player
    next_free_space = next((i for i, c in enumerate(next_game_data) if c == ' '), None)
    next_player_id = (player_id + 1) % 2 if next_free_space is not None else None

    # check for win
    win_player_id = player_id if check_for_winner(next_game_data, player_id) else None

    return next_game_data, next_player_id, win_player_id

def check_for_winner(game_data, player_id):
    player_symbol = get_player_symbol(player_id)
    for index in range(0, width * height):
        symbol = game_data[index]
        if symbol != player_symbol: continue
        if check_connection(game_data, index, (1, -1)): return True
        if check_connection(game_data, index, (1, 0)): return True
        if check_connection(game_data, index, (1, 1)): return True
        if check_connection(game_data, index, (0, 1)): return True
    return False

def check_connection(game_data, start_index, direction):
    x, y = get_xy(start_index)
    if x < 0 or x + connect_length * direction[0] >= width: return False
    if y < 0 or y + connect_length * direction[1] >= height: return False
    symbol = game_data[start_index]
    for i in range(1, connect_length):
        test_index = get_index(x + i * direction[0], y + i * direction[1])
        test_symbol = game_data[test_index]
        if symbol != test_symbol: return False
    return True

def get_player_symbol(player_id):
    return 'R' if player_id == 0 else 'Y'

def get_player_id(player_symbol):
    return 0 if player_symbol == 'R' else 1

def get_index(x, y):
    return x + y * width

def get_xy(index):
    x = int(index % width)
    y = int((index / width) % height)
    return x, y