"""
Strings and Conditional
"""

favorite_fruit = "blueberry"
counter = 0
for character in favorite_fruit:
  if character == "b":
    counter = counter + 1
print(counter) #out: 2

"""
Write a function called that takes two inputs, word and letter.
This function should return True if the word contains the letter and False if it does not.
"""

def letter_check(word, letter):
  for character in word:
    if character == letter:
      return print(True)
  return print(False)

letter_check("strawberry", "a") #out: True
letter_check("strawberry", "o") #out: False

"""
Function takes two arguments, and returns True if big_string contains little_string.
"""

def contains(big_string, little_string):
  return print(little_string in big_string)

contains("watermelon", "melon") #out: True
contains("watermelon", "berry") #out: False

"""
Function takes two arguments, and returns a list with all of the letters they have in common.
The letters in the returned list should be unique.
"""

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return print(common) #['a']

common_letters("banana", "cream")

