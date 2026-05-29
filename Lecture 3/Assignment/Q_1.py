# Sort a list of tuples based on tuple values, without defining a function

items = [(3, 7), (1, 4), (5, 2), (2, 9)]

# Sort by the first tuple value
items.sort(key=lambda x: x[0])
print("Sorted by first value:", items)

# Sort by the second tuple value
items = [(3, 7), (1, 4), (5, 2), (2, 9)]
items.sort(key=lambda x: x[1])
print("Sorted by second value:", items)
