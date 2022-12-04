from string import ascii_lowercase as alphabet


with open("./input.txt", "r") as file:

    lines = [line.strip() for line in file.readlines()]

    priority_scale = alphabet + alphabet.upper()

    prioritysum = 0
    for line in lines:

        lhalf = line[: len(line) // 2]

        rhalf = line[len(line) // 2 :]
        for item in lhalf:
            if item in rhalf:
                prioritysum += priority_scale.index(item) + 1

    print(prioritysum)
