import random
import statistics

amountOfTries = 0
amountOfTriesList = []

for i in range(0, 1001):
    random_number = random.randrange(0, 101)
    amountOfTries = 0

    while random_number != 69:
        amountOfTries += 1
        random_number = random.randrange(0, 101)
    amountOfTriesList.append(amountOfTries)

averageAmountOfTries = int(statistics.mean(amountOfTriesList))

print("The average amount of tries was %s." % averageAmountOfTries)
