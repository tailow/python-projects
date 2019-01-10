# RATING SYSTEM SIMULATION

import random
from matplotlib import pyplot as plt

# pls don't go above 1 000 000
amount_of_players = 100000
amount_of_games = amount_of_players * 20


class Player:
    def __init__(self, name, skill, rating):
        self.name = name
        self.skill = skill
        self.rating = rating
        self.wins = 0
        self.losses = 0

    def gain_rating(self, opponent_rating):
        difference = (self.rating - opponent_rating)

        # Add rating based on opponent rating and player rating
        self.rating += -(difference**(1/3)) + 10
        self.wins += 1

    def lose_rating(self, opponent_rating):
        difference = (self.rating - opponent_rating)

        # Lose rating based on opponent rating and player rating
        self.rating -= difference**(1/3) + 5

        # Set minimum rating to 1000
        if self.rating.real < 1000:
            self.rating = 1000

        self.losses += 1


def create_players(player_count):
    for player_index in range(player_count):

        # Add a player with a random skill level
        player_object = Player(player_index, random.randrange(1000, 3000), 1500)
        players.append(player_object)


def play_game(p1, p2):

    # If opponent is self, cancel game
    if p1 == p2:
        return

    # If rating gap is higher than 50, cancel game
    if abs(p1.rating - p2.rating) >= 50:
        return

    skill_difference = p1.skill - p2.skill

    # Calculate winning odds based on skill difference
    if skill_difference > 100:
        p1_odds = 100

    elif skill_difference < -100:
        p1_odds = 0

    else:
        p1_odds = (skill_difference / 2) + 50

    # Determine winner
    if random.randint(1, 100) <= p1_odds:
        p1.gain_rating(p2.rating)
        p2.lose_rating(p1.rating)

    else:
        p2.gain_rating(p1.rating)
        p1.lose_rating(p2.rating)


players = []

create_players(amount_of_players)

# Match 2 random player against each other
for i in range(amount_of_games):
    play_game(random.choice(players), random.choice(players))

player_ratings = []
player_skills = []

# Print player stats
for player in players:
    win_ratio = int(player.wins / (player.wins + player.losses) * 100)
    player_data = ["ID: " + str(player.name), "RATING: " + str(int(player.rating.real)), "SKILL: " + str(player.skill),
                   "WINS: " + str(player.wins), "LOSSES: " + str(player.losses), "W/L RATIO: " + str(win_ratio) + " %"]

    print("{:<16} {:<16} {:<16} {:<16} {:<16} {:<16}".format(
        player_data[0], player_data[1], player_data[2], player_data[3], player_data[4], player_data[5]))

    player_ratings.append(player.rating.real)
    player_skills.append(player.skill)

# Plot player stats
fig = plt.figure(figsize=(12, 6))

fig.add_subplot(1, 2, 1)
plt.title("Player rating")
plt.hist(player_ratings, 200)

fig.add_subplot(1, 2, 2)
plt.title("Player skill")
plt.hist(player_skills, 200)

plt.show()
