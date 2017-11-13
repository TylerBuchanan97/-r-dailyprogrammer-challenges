lines = open("challenge.txt", "r").readlines()

name = "none"
salary = "none"
highest_paid = ["none", 0]

for line in lines:
    _line = line.strip()
    if _line[:7] != "::EXT::":
        salary = "none"
        name = _line[:20].strip()
    else:
        if _line[:10] == "::EXT::SAL":
            salary = int(_line[11:])

    if salary != "none":
        if highest_paid[1] < salary:
            highest_paid = [name, salary]

print("{}, ${:,}".format(highest_paid[0], highest_paid[1]))

