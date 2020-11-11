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
    if current_game_state[index] != ' ': return None
    player_char = 'O' if player_id == 0 else 'X'
    next_game_state = current_game_state[:index] + player_char + current_game_state[index+1:]
    next_player_id = (player_id + 1) % 2

    win_player_icon = check_has_won(next_game_state)
    win_player_id = None
    if win_player_icon is not None:
        win_player_id = 0 if win_player_icon == 'O' else 1

    return next_game_state, next_player_id, win_player_id

def check_has_won(game_data):
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
            return player_icon
    return None