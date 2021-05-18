"""
Return the count of how many numbers in the list are divisible by 10.
"""

def divisible_by_ten(nums):
  count = 0
  for num in nums:
     if (num % 10 == 0):
       count +=1
  return count

print(divisible_by_ten([20, 25, 30, 35, 40]))

"""
Create an empty list that will contain each greeting. 
Add the string 'Hello, ' in front of each name in names and append the greeting to the list.
Return the new list containing the greetings.
"""

def add_greetings(names):
  greeting = []
  for name in names:
    greeting.append('Hello, ' + name)
  return greeting

print(add_greetings(["Owen", "Max", "Sophie"]))

"""
The function should remove elements from the front of lst until the front of the list is not even. 
The function should then return lst.
For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].
"""

def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

"""
The function should create a new empty list and add every element from lst that has an odd index. 
The function should then return this new list.
For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].
"""

def odd_indices(lst):
  indices = []
  for index in range(1, len(lst), 2):
    indices.append(lst[index])
  return indices

print(odd_indices([4, 3, 7, 10, 11, -2]))
