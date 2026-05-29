# List Comprehensions. 
# [output for item in iterable if condition ]

squares = []

for i in range(6):
    squares.append(i*i)
print(squares)

sq = [i*i for i in range(6)]
sqodd = [i*i for i in range(6) if i%2 !=0]
print(sqodd)

