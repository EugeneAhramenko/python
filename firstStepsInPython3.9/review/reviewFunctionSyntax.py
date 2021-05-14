"""
If base raised to the exponent is greater than 5000, return True, otherwise return False
"""

def large_power(base, exponent):
  if base ** exponent > 5000:
    return True
  else:
    return False

print(large_power(2, 13))
# print True
print(large_power(2, 12))
# print False

"""
The function should return True if budget is less than the sum of the other four parameters. Return False otherwise.
"""

def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  if (budget < food_bill + electricity_bill + internet_bill + rent):
    return True
  else:
    return False

print(over_budget(100, 20, 30, 10, 40))
# print False
print(over_budget(80, 20, 30, 10, 30))
# print True

"""
Return True if num1 is more than double num2. Return False otherwise.
"""

def twice_as_large(num1, num2):
  if num1 > num2 * 2:
    return True
  else:
    return False

print(twice_as_large(10, 5))
# print False
print(twice_as_large(11, 5))
# print True

"""
The function should return True if num is divisible by 10, and False otherwise.
"""

def divisible_by_ten(num):
  if (num % 10 == 0):
    return True
  else:
    return False

print(divisible_by_ten(20))
# print True
print(divisible_by_ten(25))
# print False

"""
Return True if num1 and num2 do not sum to 10. Return False otherwise.
"""

def not_sum_to_ten(num1, num2):
    if (num1 + num2 != 10):
        return True
    else:
        return False

print(not_sum_to_ten(9, -1))
# print True
print(not_sum_to_ten(9, 1))
# print False
print(not_sum_to_ten(5, 5))
# print False