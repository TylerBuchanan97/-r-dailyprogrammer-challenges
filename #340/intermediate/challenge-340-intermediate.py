minefield = open("minefield.txt", "r").readlines()

robot_running = False
win = False

current_location = [6, 0]
last_location = current_location

for lines in minefield:
    print(lines.strip())

movement = input()

if movement[0] == "I":
    for step in movement:
        if step == "I":
            robot_running = True
        elif step == "-":
            robot_running = False

        if robot_running:
            if step == "N":
                last_location = current_location
                current_location = [current_location[0] - 1, current_location[1]] 
            elif step == "S":
                last_location = current_location
                current_location = [current_location[0] + 1, current_location[1]] 
            elif step == "E":
                last_location = current_location
                current_location = [current_location[0], current_location[1] + 1] 
            elif step == "O":
                last_location = current_location
                current_location = [current_location[0], current_location[1] - 1]

        try:        
            if minefield[current_location[0]][current_location[1]] == "+":
                current_location = last_location
            elif minefield[current_location[0]][current_location[1]] == " ":
                current_location = last_location
            elif minefield[current_location[0]][current_location[1]] == "*":
                print("You exploded!")
                break
        except IndexError:
            current_location = last_location

        if current_location == [1, 11]:
            if step == "-":
                print("Robot shut off at exit, success!")
                win = True
                break
        
else:
    print("You never started the robot!")

if not win:
    print("You did not get to the exit!")
