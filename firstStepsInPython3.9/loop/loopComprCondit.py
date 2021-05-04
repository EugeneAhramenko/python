"""
Conditionals to list comprehension:

1. Takes an element in the list numbers.
2. Assigns that element to a variable called num.
3. Checks if the condition num < 0 is met by the element stored in num. If so, it goes to step 4, otherwise it skips it
and goes to the next element in the list.
4. Applies the expression num * 2 on the element stored in num and adds the result to a new list called negative_doubled
5. Repeats steps 1-3 (and sometimes 4) for every other element in the numbers list.

We can also use If-Else conditions directly in our comprehensions. For example, let’s say we wanted to double every
negative number but triple all positive numbers. Here is what our code might look like:

Our result would be the same: [6, -2, 237, 99, -90]

a = []
for x in range(10):
    a.append(x * 10)

VS

a = [x * 10 for x in range(10)]

"""
numbers = [2, -1, 79, 33, -45]
only_negative_doubled = []

for num in numbers:
    if num < 0:
        only_negative_doubled.append(num * 2)

print(only_negative_doubled)

"""
This is a bit different than our previous comprehension since the conditional if num < 0 else num * 3 comes after 
the expression num * 2 but before our for keyword.
"""

numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 if num < 0 else num * 3 for num in numbers ]
print(doubled)

# OR

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [heigh for heigh in heights if heigh > 161]
print(can_ride_coaster)

