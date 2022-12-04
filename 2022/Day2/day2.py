with open("./input.txt", "r") as file:
  lines = [line.strip() for line in file.readlines()]

  score = 0
  for line in lines:
    opponent_move, own_move = line.split(" ")
    if own_move == "X":
      score += 1
      if opponent_move == "A":
        score += 3
      elif opponent_move == "C":
        score += 6
    elif own_move == "Y":
      score += 2
      if opponent_move == "B":
        score += 3
      elif opponent_move == "A":
        score += 6
    elif own_move == "Z":
      score += 3
      if opponent_move == "C":
        score += 3
      elif opponent_move == "B":
        score += 6
  
  print(score)