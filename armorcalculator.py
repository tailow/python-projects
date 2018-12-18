class Gloves:
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight


class Chest:
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight


class Boots:
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight


class Helmet:
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight


def check_values():
    name = input("Input name: ")
    value = int(input("Input value: "))
    weight = int(input("Input weight: "))

    return Gloves(name, value, weight)


def check_highest_value(max_weight):
    highest_value = 0
    best_combination = []

    for glove in glove_list:
        for chest in chest_list:
            for boot in boot_list:
                for helm in helm_list:
                    value_sum = glove.value + chest.value + boot.value + helm.value
                    weight_sum = glove.weight + chest.weight + boot.weight + helm.weight

                    if value_sum > highest_value and weight_sum <= max_weight:
                        highest_value = value_sum

                        best_combination = [glove, chest, boot, helm]

    return best_combination


glove_list = []
chest_list = []
boot_list = []
helm_list = []


while True:
    user_input = input("ARMOR TYPE (G/C/B/H): ")

    if user_input == "G":
        glove_list.append(check_values())
    elif user_input == "C":
        chest_list.append(check_values())
    elif user_input == "B":
        boot_list.append(check_values())
    elif user_input == "H":
        helm_list.append(check_values())

    if input("Would you like to add a new item? (Y/N): ") == "Y":
        continue
    else:
        break

best_items = check_highest_value(int(input("Max weight: ")))

if not best_items:
    print("No good combination")

else:
    print()
    print("The best items are {0}, {1}, {2}, {3}.".format
          (best_items[0].name, best_items[1].name, best_items[2].name, best_items[3].name))
    print("Weight: ", best_items[0].weight + best_items[1].weight + best_items[2].weight + best_items[3].weight)
    print("Value: ", best_items[0].value + best_items[1].value + best_items[2].value + best_items[3].value)
