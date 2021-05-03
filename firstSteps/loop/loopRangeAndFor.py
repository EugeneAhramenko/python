"""
For Loops:
for <temporary variable> in <collection>:
  <action>
"""

board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]
sport_games = ["football", "hockey", "baseball", "cricket"]

for bgame in board_games:
  print(bgame)

for sgame in sport_games:
  print(sgame)

# Using Range:
promise = "I will finish the python loops module!"

for temporary in range(5):
  print(promise)

# While Loops:
