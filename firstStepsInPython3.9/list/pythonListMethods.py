# Adding by Index:
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
front_display_list.insert(0, "Pineapple")
print(front_display_list)

# Removing by Index: Pop:
data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
data_science_topics.pop()
data_science_topics.pop(3)
print(data_science_topics)

# Consecutive Lists: Range:
number_list = range(9)
print(list(number_list))
zero_to_seven = range(8)
print(list(zero_to_seven))

# The Power of Range!:
range_five_three = range(5, 15, 3)
print(list(range_five_three))
range_diff_five = range(0, 40, 5)
print(list(range_diff_five))

# Length:
long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice",
             "getting", "the", "length"]
long_list_len = len(long_list)
print(long_list_len)

range_list = range(2, 3000, 100)
range_list_length = len(range_list)
print(range_list_length)

#  Slicing Lists I
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
beginning = suitcase[0:2]
middle = suitcase[2:4]
print(beginning)
print(middle)

# Slicing Lists II
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
last_two_elements = suitcase[-2:]
slice_off_last_three = suitcase[:-3]
print(last_two_elements)
print(slice_off_last_three)

# Counting in a List
votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake",
         "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]
jake_votes = votes.count("Jake")
print(jake_votes)

# Sorting Lists I
# Sorting Lists I:
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace",
             "1600 Pennsylvania Ave", "10 Downing St."]
addresses.sort()
print(addresses)

cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort(reverse=True)
print(sorted_cities)

# Sorting Lists II:
games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]
games_sorted = sorted(games)
print(games)
print(games_sorted)

"""
Return a new list containing every number in bases raised to every number in powers.
For example, consider the following code: exponents([2, 3, 4], [1, 2, 3])
the result would be the list [2, 4, 8, 3, 9, 27, 4, 16, 64]. 
It would first add two to the first. Then two to the second. Then two to the third, and so on.
"""

def exponents(bases, powers):
  answers = []
  for base in bases:
    for power in powers:
      answers.append(base ** power)
  return answers

print(exponents([2, 3, 4], [1, 2, 3]))
