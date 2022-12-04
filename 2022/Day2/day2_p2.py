scores = {
  "A": 1,
  "B": 2,
  "C": 3
}

counters = {
  "A": "B",
  "B": "C",
  "C": "A"
}

with open("./input.txt", "r") as file:
  lines = [line.strip() for line in file.readlines()]

  score = 0
  for line in lines:
    opponent_move, outcome = line.split(" ")
    # loss
    if outcome == "X":
      score += scores["ABC".replace(opponent_move, "").replace(counters[opponent_move], "")]
    # draw
    elif outcome == "Y":
      score += (scores[opponent_move] + 3)
    # win
    elif outcome == "Z":
      score += (6 + scores[counters[opponent_move]])  
  print(score)