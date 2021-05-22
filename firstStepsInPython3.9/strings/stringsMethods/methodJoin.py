"""
Joining Strings
.join() to combine these words into a sentence and save that sentence as the string
"""

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
print(" ".join(reapers_line_one_words)) # => Black reapers with the sound of steel on stones

print("------")

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!',
                      'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds',
                      'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

print('\n'.join(winter_trees_lines))
# =>
# All the complicated details
# of the attiring and
# the disattiring are completed!
# A liquid moon
# moves gently among
# the long branches.
# Thus having prepared their buds
# against a sure winter
# the wise trees
# stand sleeping in the cold.
