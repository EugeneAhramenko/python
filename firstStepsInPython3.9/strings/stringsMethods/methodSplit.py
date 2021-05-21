"""
.split() is performed on a string, takes one argument, and returns a list of substrings found between the given argument
 (which in the case of .split() is known as the delimiter).
 string_name.split(delimiter)
"""

line_one = "The sky has given over"
print(line_one.split()) # => ['The', 'sky', 'has', 'given', 'over']

print("------")

"""
Using .split() and the provided string, create a list called author_names containing each individual author name as it’s
own string.
Create another list called author_last_names that only contains the last names of the poets in the provided string.
"""

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa," \
          "Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')
print(author_names)
# => ['Audre Lorde', 'Gabriela Mistral', 'Jean Toomer', 'An Qi', 'Walt Whitman', 'Shel Silverstein',
# 'Carmen Boullosa', 'Kamala Suraiyya', 'Langston Hughes', 'Adrienne Rich', 'Nikki Giovanni']

author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])
print(author_last_names) # => ['Lorde', 'Mistral', 'Toomer', 'Qi', 'Whitman', 'Silverstein', 'Boullosa', 'Suraiyya',
# 'Hughes', 'Rich', 'Giovanni']

print("------")

"""
\n Newline
\t Horizontal Tab
"""

spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

print(spring_storm_text.split('\n')) # => ['The sky has given over ', 'its bitterness. ', 'Out of the dark change ',
# 'all day long ', 'rain falls and falls ', 'as if it would never end. ', 'Still the snow keeps ',
# 'its hold on the ground. ', 'But water, water ', 'from a thousand runnels! ', 'It collects swiftly, ',
# 'dappled with black ', 'cuts a way for itself ', 'through green ice in the gutters. ', 'Drop after drop it falls ',
# 'from the withered grass-stems ', 'of the overhanging embankment.']

