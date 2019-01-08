import random

num_list = []

for i in range(100000):
    random_num = random.randrange(0, 9)

    num_list.append(random_num)

    if i > 4:
        if num_list[i] == num_list[i - 1] == num_list[i - 2] == num_list[i - 3] == num_list[i - 4]:
            print(i)
            break