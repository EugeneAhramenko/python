"""
Calling a function:
"""

def directions_to_timesSq():
    print("Walk 4 mins to 34th St Herald Square train station.")
    print("Take the Northbound N, Q, R, or W train 1 stop.")
    print("Get off the Times Square 42nd Street stop.")
    print("Take lots of pictures!")


directions_to_timesSq()

"""
Whitespace & Execution Flow:
"""

print("Checking the weather for you!")  # 1 output


def weather_check():
    print("Looks great outside! Enjoy your trip.") # 3 output


print("False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.")
# 2 output

weather_check()

"""
Parameters & Arguments:
"""

def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit " + location)
  print("You can use the public subway system to get to " + location)

generate_trip_instructions("Grand Central Station")

"""
Multiple Parameters:
"""

def calculate_expenses (plane_ticket_price, car_rental_rate, hotel_rate,
trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  print(car_rental_total + hotel_total + plane_ticket_price)

calculate_expenses(200, 100, 100, 5)

"""
Types of Arguments:
"""

def trip_planner(first_destination, second_destination, final_destination = "Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + ", then " +    second_destination + ", and lastly " + final_destination)

trip_planner("Brooklyn",second_destination="Queens")

"""
Built-in Functions vs User Defined Functions
"""

tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

max_price = max(tshirt_price, shorts_price, mug_price, poster_price)
print(max_price)

min_price = min(tshirt_price, shorts_price, mug_price, poster_price)
print(min_price)

rounded_price = round(tshirt_price, 1)
print(rounded_price)

"""
Variable Access
"""

# This function will print a hardcoded count of how many locations we have.
def print_count_locations():
    print("There are 3 locations")

# This function will print the favorite locations
def show_favorite_locations():
    favorite_locations = "Paris, Norway, Iceland"
    print("Your favorite locations are: " + favorite_locations)


print_count_locations()
show_favorite_locations()

"""
Returns
"""

current_budget = 3500.75

def print_remaining_budget(budget):
    print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

def deduct_expense(budget, expense):
    return budget - expense


shirt_expense = 9

new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)

"""
Multiple Returns
"""

def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third

most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)

"""
Review
"""

def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + name)

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

trip_planner_welcome("3.9")
estimate = estimated_time_rounded(2.43)
destination_setup("Python", "3.9 ", estimate, "Car")

