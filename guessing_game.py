import random

secret= random.randint(1, 50)

counter= 0

try:
    guess = int(input("Guess a number between 1 and 50: "))
except ValueError:
    print("Please enter a number, not a word!")
    guess = int(input("Guess a number between 1 and 50: "))

while guess != secret:
    if guess < 1 or guess >  50:
       print("Invalid number! Enter between 1 and 50")
    elif guess > secret:
        print("Too high! Try again!")
    else:
        print("Too low! Try again") 
    try:
        guess = int(input("Guess a number between 1 and 50: "))
    except ValueError:
        print("Please enter a number, not a word!")
        guess = int(input("Try again: "))
    counter = counter + 1

print("Correct! 🎉:You got it in : ", counter, "Times")
# Already up to date.
