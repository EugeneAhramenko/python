"""
The function should return True if num is greater than or equal to lower and less than or equal to upper.
Otherwise, return False.
"""

def in_range(num, lower, upper):
  if (num >= lower and num <= upper):
    return True
  else:
    return False

print(in_range(10, 10, 10))
# print True
print(in_range(5, 10, 20))
# print False

"""
If our names are identical, return True. Otherwise, return False.
"""

def same_name(your_name, my_name):
  if (your_name == my_name):
    return True
  else:
    return False

print(same_name("Colby", "Colby"))
# print True
print(same_name("Tina", "Amber"))
# print False

"""
Using an if statement, your variable num, and the operators >, and <, make it so your function will return False no 
matter what number is stored in num.
An if statement that is always false is called a contradiction.
"""

def always_false(num):
  if (num > 0 and num < 0):
    return True
  else:
    return False

print(always_false(0))
# print False
print(always_false(-1))
# print False
print(always_false(1))
# print False

"""
If rating is less than or equal to 5, return "Avoid at all costs!". If rating is between 5 and 9, return 
"This one was fun.". If rating is 9 or above, return "Outstanding!"
"""

def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  if (rating > 5 and rating < 9):
    return "This one was fun."
  if rating >= 9:
    return "Outstanding!"

# Second solution:
def movie_review_1(rating):
  if(rating <= 5):
    return "Avoid at all costs!"
  if(rating < 9):
    return "This one was fun."
  return "Outstanding!"

print(movie_review(9))
# print "Outstanding!"
print(movie_review(4))
# print "Avoid at all costs!"
print(movie_review(6))
# print "This one was fun."

"""
The function should return the largest of these three numbers. If any of two numbers tie as the largest, 
you should return "It's a tie!".
"""

def max_num(num1, num2, num3):
  if (num1 > num2 and num1 > num3):
    return num1
  elif (num2 > num1 and num2 > num3):
    return num2
  elif (num3 > num1 and num3 > num2):
    return num3
  else:
    return "It's a tie!"

print(max_num(-10, 0, 10))
# print 10
print(max_num(-10, 5, -30))
# print 5
print(max_num(-5, -10, -10))
# print -5
print(max_num(2, 3, 3))
# print "It's a tie!"
