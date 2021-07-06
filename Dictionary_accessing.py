# Today we will learn about the accessing a dictionary from a list of dictionary

# Here is our list of dict
orders = {"apple":5,"banana":3,"grapes":2}

# if we print simple value of oreders then it will show us the type too
print(orders.values())
# Here we clarify that we need outout in form of list
print(list(orders.values()))
# Here  we try to get output in tuple form
for tuple in list(orders.items()):
  print(tuple)
