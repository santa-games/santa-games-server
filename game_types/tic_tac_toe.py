options = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]

def create():
    return "         "

def turn(current_game_state, player_id, player_action):
    index = int(player_action)
    
    # check if its a valid move
    if current_game_state[index] != ' ':
        return None, None, None
    
    # get next game state
    player_char = 'O' if player_id == 0 else 'X'
    next_game_state = current_game_state[:index] + player_char + current_game_state[index+1:]

    # work out the next player
    if next((i for i, c in enumerate(game_data) if c == ' '), None) is None: next_player_id = None
    else: next_player_id = (player_id + 1) % 2

    # work out if a player has won
    win_player_id = find_winning_player(next_game_state)

    return next_game_state, next_player_id, win_player_id

def find_winning_player(game_data):
    for option in options:
        player_icon = game_data[option[0]]
        if player_icon == ' ':
            continue
        success = True
        for o in option[1:]:
            if game_data[o] != player_icon:
                success = False 
                break
        if success:
            return 0 if player_icon == 'O' else 1
    return None