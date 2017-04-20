def main():
    inputs = [[4, 1, 4, 2, 3],
              [5, 1, 4, 2, -1, 6],
              [4, 19, 22, 24, 21],
              [4, 19, 22, 24, 25],
              [4, 2, -1, 0, 2]]

    differences = [[], [], [], [] ,[]]

    for a in range(len(inputs)):
        for b in range(len(inputs[a]) - 1):
            differences[a].append(abs(inputs[a][b] - inputs[a][b + 1]))

    for c in range(len(inputs)):
        for d in range(1, len(inputs[c]) - 1):
            if d not in differences[c]:
                results(differences[c], "NOT JOLLY")
                break
            else:
                results(differences[c], "JOLLY")
                break
            

def results(numbers, jolly):
    for x in range(len(numbers)):
        print(numbers[x], end=" ")
    print(jolly)

main()
