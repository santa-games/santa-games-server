# Santa-Games: santa-games-server

This repository contains the server/API code which provides the back-end functionality of Santa-Games. Santa-Games is a hub which allows users to compete by playing simple strategy/zero-sum games against each other. The intent is to allow users to write AI to actually play the games, and the competition is in writing the most successful AI, however it is also possible to play the games manually via the API.

# Getting Started

If you want to setup a local version of the server to test you're AI against, or to develop  additional capability via a PR, first you need to setup the database. The location to the database is configured using the `SANTA_GAMES_SQLALCHEMY_DATABASE_URI` environment variable. If running locally, a sqlite database can be used such as:

```
sqlite:///foo.db
sqlite:///C://foo.db
sqlite:///C://foo.bar
```

> Note: you don't need to use the .db extension, any extension can be used here. 

Other database connection strings are detailed here [https://docs.sqlalchemy.org/en/13/core/engines.html]

Running the server once the database is configured is as simple as:

``` bash
python ./app.py
```
This will state a localhost server which you can test against.

## Game Types

Currently Santa-Games only fully supports Tic-tac-toe, and Connect-4 is in development. We have aspirations to add additional games depending on interest. Potential future additions include:

- Othello
- Squares game
- Draughts
- Chess
- Order & Chaos (A variant of Tic-tac-toe)

If you have any suggestions/requests please let us know.

## Contributions

We're very keen for contributions, and if you'd like to add a capability to Santa-Games (e.g. a new game type) then take a branch and put in a PR. It's probably worth sending us a message of what you're intending so we can advise the best way to do it. 

Likewise, we're keen for contributions to the other aspects of Santa-Games, such as the website or example bots.

## API

In lieu of swagger documentation, the current end-points are:

| Verb | URI                       | Description             |
|------|---------------------------|-------------------------|
| GET  | /api/users                | Get a list of the users | 
| POST | /api/users                | Register a new user     |
| GET  | /api/games                | Get a list of games     |
| POST | /api/games                | Propose a new game      |
| PUT  | /api/games/:game_id       | Accept a proposed game  |
| POST | /api/games/:game_id/turns | Take a turn             |

At some point we'll get around to adding swagger...

## Licence

All the Santa-Games repositories are MIT.