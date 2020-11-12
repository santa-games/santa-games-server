# santa-games-server
API providing functionality to play games against other opponents (AI/Human)

## Endpoints
GET     /api/users                  Get a list of the users
POST    /api/users                  Register a new user

GET     /api/games                  Get a list of games
POST    /api/games                  Propose a new game

PUT     /api/games/:game_id         Accept a proposed game
POST    /api/games/:game_id/turns   Take a turn

## Game ideas
- othello
- squares game
- draughts/chess
- connect 4
- order & chaos (tic-tac-toe mod)
