inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table",
             "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow",
             "pillow"]

#  Count items:
inventory_len = len(inventory)
print(inventory_len)

#  Select first item:
first = inventory[1]
print(first)

#  Select last item:
last = inventory[-1]
print(last)

# Select items using interval:
inventory_2_6 = inventory[2:6]
print(inventory_2_6)

# Select first 3 items:
first_3 = inventory[:3]
print(first_3)

# Count items:
twin_beds = inventory.count('twin bed')
print(twin_beds)

# Remove item:
removed_item = inventory.pop(4)
print(removed_item)

# Insert item as the 11th element
inventory.insert(10, "19th Century Bed Frame")

# Sort and Sorted:
inventory.sort()
inentory_sorted = sorted(inventory)
print(inventory)
print(inentory_sorted)