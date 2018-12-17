import random


print("your circumference is %s" % 69)

money = int(input("How much money would you like to start with? "))

while money > 0:
    print("You have %s dollars" % money)

    bet = int(input("How much would you like to bet? "))

    if random.randint(1, 100) < 50:
        print("You lucky bastard!")
        money += bet
        break

    else:
        print("You lost!")
        money -= bet

if money > 0:
    print("gtfo")

else:
    print("no money get out")

if money == 0:
    print()

elif money != 1:
    print()

elif money <= -2:
    print()

else:
    print()