marks = [99, 89, 100, 65, 92, "akhilesh"]

print("Original list:", marks)

# List indexing starts from 0.
# The last valid index is always len(list) - 1.
# Example: print(marks[6]) will raise IndexError because index 6 does not exist.
print("Length of the list:", len(marks))

# Lists are mutable, so we can change their values after creation.
# A list can also store different data types.
marks[2] = 96

print("List after updating index 2:", marks)

# List slicing works like string slicing.
print("First 5 elements:", marks[:5])
print("Elements from index 4 to the end:", marks[4:])
