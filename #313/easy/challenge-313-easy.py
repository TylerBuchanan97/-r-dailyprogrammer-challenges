sequence = input("Enter your sequence: ")

sequence_list = sequence[1:len(sequence)-1].split(", ")

subset_sum = False

for element in sequence_list:
    for other in sequence_list:
        if int(element) + int(other) == 0:
            subset_sum = True

print(str(subset_sum))
