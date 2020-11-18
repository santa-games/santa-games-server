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

name = "tic-tac-toe"

def create():
    return "         "

def turn(game_data, player_id, player_action):
    index = int(player_action)
    
    # check if its a valid move
    if game_data[index] != ' ':
        return None, None, None
    
    # get next game state
    player_char = 'O' if player_id == 0 else 'X'
    next_game_data = game_data[:index] + player_char + game_data[index+1:]

    # work out if a player has won
    win_player_id = check_for_winner(next_game_data)

    # work out the next player
    if win_player_id is None:
        next_free_space = next((i for i, c in enumerate(next_game_data) if c == ' '), None)
        if next_free_space is None: next_player_id = None
        else: next_player_id = (player_id + 1) % 2
    else:
        next_player_id = None

    return next_game_data, next_player_id, win_player_id

def check_for_winner(game_data):
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