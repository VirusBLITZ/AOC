from string import ascii_lowercase as alphabet


with open("./input.txt", "r") as file:

    lines = [line.strip() for line in file.readlines()]

    priority_scale = alphabet + alphabet.upper()

    prioritysum = 0
    for i in range(0, len(lines), 3):
        line = lines[i]
        for item in line:
            if item in lines[i+1] and item in lines[i+2]:
                prioritysum += priority_scale.index(item) + 1
                break

    print(prioritysum)
