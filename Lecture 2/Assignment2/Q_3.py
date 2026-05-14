# Q3. Wrie a functioni that prints the digits of number n in to reversed order. 
def print_digits(num):
    while num > 0:
        digit = num % 10      
        print(digit)
        num = num // 10

num = int(input("enter number. "))
print_digits(num)
