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

def turn(game_data, player_id, player_action):
    index = int(player_action)
    
    # check if its a valid move
    if game_data[index] != ' ':
        return None, None, None
    
    # get next game state
    player_char = 'O' if player_id == 0 else 'X'
    next_game_data = game_data[:index] + player_char + game_data[index+1:]

    # work out the next player
    next_free_space = next((i for i, c in enumerate(next_game_data) if c == ' '), None)
    print(f"Next free spot is [{next_free_space}]")
    if next_free_space is None: next_player_id = None
    else: next_player_id = (player_id + 1) % 2

    # work out if a player has won
    win_player_id = find_winning_player(next_game_data)

    return next_game_data, next_player_id, win_player_id

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