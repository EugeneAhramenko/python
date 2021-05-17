"""
The function should return a list of every third number between start and 100 (inclusive).
For example, every_three_nums(91) should return the list [91, 94, 97, 100].
If start is greater than 100, the function should return an empty list.
"""

def every_three_nums(start):
    return list(range(start, 101, 3))

print(every_three_nums(91))

"""
The function should return a list where all elements in lst with an index between start and 
end (inclusive) have been removed.
"""

def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

"""
Return either item1 or item2 depending on which item appears more often in lst.
If the two items appear the same number of times, return item1.
"""

def more_frequent_item(lst, item1, item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  else:
    return item2

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

"""
The function should return a new list where all elements are the same as in lst except for the element at index. 
The element at index should be double the value of the element at index of the original lst.
If index is not a valid index, the function should return the original list.
"""

def double_index(lst, index):
  # Checks to see if index is too big
  if index >= len(lst):
    return lst
  else:
    # Gets the original list up to index
    new_lst = lst[0:index]
  # Adds double the value at index to the new list
  new_lst.append(lst[index]*2)
  #  Adds the rest of the original list
  new_lst = new_lst + lst[index+1:]
  return new_lst

print(double_index([3, 8, -10, 12], 2))

"""
If there are an odd number of elements in lst, the function should return the middle element. 
If there are an even number of elements, the function should return the average of the middle two elements.
"""

def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

print(middle_element([5, 2, -10, -4, 4, 5]))

"""
NOTE:
When we divide by 2, we would get a double. 
For example, if our list had 3 items in it, then 3/2 would give us 1.5. 
The middle index should be 1, so in order to go from 1.5 to 1, 
we cast 1.5 as an int. In total, this is int(len(lst)/2).
"""