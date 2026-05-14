# Q6. Write a program to swap values of two numbers entered by the user. 

a = int(input("enter number a :"))
b = int(input("enter number b :"))

print("Before swapping ",a ,",",b)

c = b
b = a
a = c

print("After swapping =" , a, " ," ,b)