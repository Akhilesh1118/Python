# Letʼs create a Simple Calculator that performs arithmetic operations. Create 
# a function calculator(a, b, operation) that performs addition, subtraction, 
# multiplication, or division based on the operation parameter. 
# [operation] 
# operation 
# parameter can have values '+', '-', '*'& "/". 

def calculator(a, b, operation):

    if operation == "+":
        return a + b

    elif operation == "-":
        return a - b

    elif operation == "*":
        return a * b

    elif operation == "/":
        if b != 0:
            return a / b
        else:
            return "Division by zero is not allowed"

    else:
        return "Invalid Operation"


# User Input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Function Call
result = calculator(a, b, operation)

print("Result =", result)