def cal_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *=  i

    return fact
n = int(input("Calculate the given number factorial .  "))    
number = cal_factorial(n)
print(number)