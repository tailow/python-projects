import random
import string

random_letters = []
letters = string.ascii_lowercase

i = 0

while i < 100000000:
    random_letters.append(random.choice(letters))
    i += 1

test_file = open("C:\\Users\\revit\\Desktop\\Projektit\\Python\\test_project\\testfile.txt", "w")

for letter in random_letters:
    test_file.write(letter)