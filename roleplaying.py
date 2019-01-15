# TEXT BASED RPG

import random

attack_level = 1
strength_level = 1
defence_level = 1

attack_xp = 0
strength_xp = 0
defence_xp = 0

while True:
    try:
        player_input = input("You see an enemy in front of you.\n"
                             "Would you like to attack? (Y/N)")
    except ValueError:
        print("Invalid input.")
        continue

    if player_input.capitalize() == "Y":
        player_health = 50

        opponent_level = random.randint(5, 20)
        opponent_health = opponent_level

        while True:
            while True:
                try:
                    attack_type = input("What type of attack would you like to use?\n"
                                        "(ATT/STR/DEF)\n")
                    break
                except ValueError:
                    print("Invalid input.")

            hit_chance = attack_level / 20
            hit_power = strength_level
            defence = defence_level

            if attack_type.upper() == "ATT":
                hit_chance *= 1.5
                attack_xp += 100
                print(attack_level)

                if attack_xp % (attack_level * 1000) == 0:
                    attack_level += 1
                    print("\n\nYour attack level is now %s!!\n\n" % attack_level)

            elif attack_type.upper() == "STR":
                hit_power *= 1.5
                strength_xp += 100

                if strength_xp % (strength_level * 1000) == 0:
                    strength_level += 1
                    print("\n\nYour strength level is now %s!!\n\n" % strength_level)

            elif attack_type.upper() == "DEF":
                defence *= 1.5
                defence_xp += 100

                if defence_xp % (defence_level * 1000) == 0:
                    defence_level += 1
                    print("\n\nYour defence level is now %s!!\n\n" % defence_level)

            else:
                print("Invalid input.")
                continue

            damage = int(hit_power * random.uniform(1, 2))

            if hit_chance >= random.uniform(0, 1):
                opponent_health -= damage

                print("You hit the opponent for %s!" % damage)
                print("He has %s health left!\n" % opponent_health)

            else:
                print("You missed!\n")

            if opponent_health <= 0:
                print("You got a kill!\n")
                break

            opponent_damage = int(random.randint(3, 10) * opponent_level / defence / 20)
            player_health -= opponent_damage

            print("You got hit for %s damage!" % opponent_damage)
            print("You have %s health.\n" % player_health)

            if player_health <= 0:
                print("You died!\n")
                break
