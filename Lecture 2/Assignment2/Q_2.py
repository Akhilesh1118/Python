
# Q2. Write a function that takes two integers a and b  prints all even 
# numbers between them (inclusive). 

def print_even_numbers(a, b):
    for num in range(a, b +1):
        if num % 2 == 0:
            print(num)

# Example
print_even_numbers(2, 10)