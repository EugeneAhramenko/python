"""
Introduction to list comprehension:

1. Takes an element in the list numbers
2. Assigns that element to a variable called num (our <element>)
3. Applies the <expression> on the element stored in num and adds the result to a new list called doubled
4. Repeats steps 1-3 for every other element in the numbers list (our <collection>)

Our result would be the same: [4, -2, 158, 66, -90]

"""

numbers = [2, -1, 79, 33, -45]
doubled = []

for number in numbers:
    doubled.append(number * 2)

print(doubled)

# The same result but different comprehension

numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]
print(doubled)

# OR

grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [grade + 10 for grade in grades]
print(scaled_grades)