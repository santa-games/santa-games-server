

class User:
    def __init__(self, name, skill, rank):
        self.name = name
        self.skill = skill
        self.rank = rank
        self.played = 0

import random
from tabulate import tabulate

users = []
for i in range(20):
    skill = round(random.random(), 2)
    rank = 1000
    users.append(User(i, skill, rank))

game_number = 0
while game_number < 10000:
    player_a = random.choice(users)
    player_b = random.choice([user for user in users if not user is player_a])

    player_a_value = round(player_a.skill + random.random() * (1 - player_a.skill), 2)
    player_b_value = round(player_b.skill + random.random() * (1 - player_b.skill), 2)

    if player_a_value > player_b_value:
        player_a_score = 1
        player_b_score = 0
    elif player_a_value < player_b_value:
        player_a_score = 0
        player_b_score = 1
    else:
        player_a_score = 0.5
        player_b_score = 0.5

    q_a = pow(10, player_a.rank / 400)
    q_b = pow(10, player_b.rank / 400)
    e_a = q_a / (q_a + q_b)
    e_b = q_b / (q_a + q_b)
    k = 32

    player_a.rank += int(k * (player_a_score - e_a))
    player_b.rank += int(k * (player_b_score - e_b))

    player_a.played += 1
    player_b.played += 1

    game_number += 1

users.sort(key=lambda user: user.rank, reverse=True)
print(tabulate([[user.name, user.skill, user.rank, user.played] for user in users], headers=["id", "skill", "rank", "played"]))

