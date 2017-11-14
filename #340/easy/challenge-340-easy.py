my_string = input()

processing = True

for x in range(len(my_string)):
    if not processing:
        break
    for y in range(x + 1, len(my_string)):
        if my_string[x] == my_string[y]:
            print("First Reoccurring Character: {}, Index: {}".format(my_string[x], x))
            processing = False
