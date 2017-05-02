inputs = [1234, 1243, 234765, 19000]

for input_num in inputs:
    temp_num = input_num
    while True:
        temp_num += 1
        temp_list = []
        for digit in str(temp_num):
            temp_list.append(digit)
        for digit in str(input_num):
            if digit in temp_list:
                temp_list.remove(digit)
        if len(temp_list) == 0:
            print(temp_num)
            break
        
