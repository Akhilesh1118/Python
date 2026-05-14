# Q9. Ask the user for: Principal (P), Rate (R), Time (T). Convert all to and 
# compute simple interest: 
# SI = (P ∗ R ∗ T )/100 

p = int(input("Enter the Principle : "))
r = int(input("Enter the Rate : "))
t = int(input("Enter the Time : "))

si = (p*r*t) / 100 

print("SI " , si )