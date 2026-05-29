a = 5
b = 10 

sum = a+b

# Normal formating. 
print("language is {}".format("python"))
print("sum of {} & {} is {}".format(a,b,sum))

# Indexing formating. 
print("sum of {1} & {0} is {2}".format(a,b,sum))

# value based formating.
print("{a} , value of variable. {a} & {b}".format(a=10, b=50) )

# F - String it indrouce with version 3.6 of python 

print(f"sum is {a} & {b} is {a+b}")