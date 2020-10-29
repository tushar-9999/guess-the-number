#This is out first number guessing game

import random

#Defining variables

n = random.randint(1,99)
guess = int(input("Enter an integer from 1 to 99: "))

#Do a loop

while n != "guess":
    print
    if guess < n:
        print ("guess is low")
        guess = int(input("Enter an integer from 1 to 99: "))
    elif guess > n:
        print ("guess is high")
        guess = int(input("Enter an integer from 1 to 99: "))
    else:
        print ("You guessed it!")
        break
    print
