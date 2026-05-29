tup = (1,2,3,4,5)
# TUPLE are immutable no more value assgin . 
# tup[2] = 10 #TypeError: 'tuple' object does not support item assignment 
print(tup)
print(type(tup))
print(len(tup))

# print the sum of the tuple. 
sum = 0
for val in tup:
    sum += val
print(f"sum of vals is = {sum}") 