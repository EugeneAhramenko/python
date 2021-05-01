# Make Some Pizzas:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
num_pizzas = len(toppings)

prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

print("We sell " + str(num_pizzas) + " different kinds of pizaa!")

# Convert toppings and prices lists into a two-dimensional list:
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)

# Sorting and Slicing Pizzas:
pizza_and_prices.sort()

cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

#  Remove lasr
pizza_and_prices.pop(-1)

#  Insert new one
pizza_and_prices.insert(3, [2.5, "peppers"])

#  More 3 cheapest
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)

