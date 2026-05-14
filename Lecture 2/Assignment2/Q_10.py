#  Letʼs create a “Number Guessing Game”. Given a secret number (already 
# decided by you), write a program that asks the user to guess it and prints: 

secret_number = 25   # Secret no. 

while True:
    guess = int(input("Guess the number: "))

    if guess > secret_number:
        print("Too high")

    elif guess < secret_number:
        print("Too low")

    else:
        print("Correct!")
        break