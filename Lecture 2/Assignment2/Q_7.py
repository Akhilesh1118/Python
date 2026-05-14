# Design a program to continuously input a number from user & print if it is 
# positive or negative until the user enters “Quit”. 

while True:
    user_input = input("Enter a number or type 'Quit' to stop: ")

    if user_input == "Quit":
        print("Program Ended")
        break

    num = int(user_input)

    if num > 0:
        print("Positive Number")
    elif num < 0:
        print("Negative Number")
    else:
        print("Zero")