tree_height = int(input("How tall would you like this tree to be?\n"))
for i in range(0, tree_height):
    print(" " * (tree_height - i), end="")
    print("#" * (1 + (i * 2)))
print(" " * (tree_height - 1), "#")

