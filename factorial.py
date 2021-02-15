user_input = int(input())
factorial = user_input

for x in range(1, user_input):
    factorial *= x

test_file = open("testfile.txt", "w")

test_file.write(str(factorial))
