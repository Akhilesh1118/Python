# Q4. Write a function to return the count the number of digits in a number n . 

def count_digits(num):
    count = 0

    while num > 0:
        count += 1
        num = num // 10

    return count


num = int(input("enter number. "))
print(count_digits(num))