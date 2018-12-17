import random
from matplotlib import pyplot as plt


players = []


class Player:
    def __init__(self, name, skill, rating):
        self.name = name
        self.skill = skill
        self.rating = rating
        self.wins = 0
        self.losses = 0

    def gain_rating(self, opponent_rating):
        difference = (self.rating - opponent_rating)

        self.rating += -(difference**(1/3)) + 10
        self.wins += 1

    def lose_rating(self, opponent_rating):
        difference = (self.rating - opponent_rating)

        self.rating -= 1.35*difference**(1/3) + 10

        if self.rating.real < 1000:
            self.rating = 1000

        self.losses += 1


def create_players(player_count):
    for i in range(player_count):
        player = Player(i, random.randrange(1000, 3000), 1500)
        players.append(player)


def play_game(p1, p2):
    if p1 == p2:
        return

    if abs(p1.rating - p2.rating) >= 1000:
        return

    skill_difference = p1.skill - p2.skill

    if skill_difference > 500:
        p1_odds = 100

    elif skill_difference < -500:
        p1_odds = 0

    else:
        p1_odds = (skill_difference / 10) + 50

    if random.randint(1, 100) <= p1_odds:
        p1.gain_rating(p2.rating)
        p2.lose_rating(p1.rating)

    else:
        p2.gain_rating(p1.rating)
        p1.lose_rating(p2.rating)


create_players(10000)

for i in range(100000):
    play_game(random.choice(players), random.choice(players))

player_ratings = []

for player in players:
    print(player.name, int(player.rating.real), player.skill, player.wins, player.losses)
    player_ratings.append(player.rating.real)

plt.hist(player_ratings, 100)
plt.show()