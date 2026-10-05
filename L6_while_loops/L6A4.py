from random import randrange
print("Welcome to my number guessing game can YOU guess my number?")

irand = randrange(0, 11)
guess = 0

while guess != irand:
    guess= int(input("Guess a number between 1 and 10: "))

    if guess < irand:
        print("Too low try again")
    elif guess > irand:
        print("Too high try again")

print("Congrats you did it!")