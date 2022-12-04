with open("./input.txt", "r") as file:
  lines = [line.strip() for line in file.readlines()]
  
  calories = [0]
  for line in lines:
    if line == "":
      calories.append(0)
      continue
    calories[-1] += int(line)
  
  # a
  # print(max(calories))

# b
  print(sum(sorted(calories)[-3:]))