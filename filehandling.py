import random
import string

random_letters = []
letters = string.ascii_lowercase

i = 0

while i < 100000:
    random_letters.append(random.choice(letters))
    i += 1

test_file = open("testfile.txt", "w")

for letter in random_letters:
    test_file.write(letter)
