sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

for location in sales_data:
  print(location)
  for scops in location:
    scoops_sold += scops
print(scoops_sold)

print("------")

for y in range(5):
    for x in range(5):
        print ("X ", end='')
    print ()