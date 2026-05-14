# Q5. Write a function to return the sum of digits of a number, n. 

def sum_of_digits(num):
    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10       

    return total

# Example
print(sum_of_digits(312))