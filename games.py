# This Python script implements a number guessing game using basic control structures.
#  It uses random.randrange(100) to generate a target number between 0 and 99. The user 
#  is given 7 attempts to guess the number. A while loop handles repeated input, and conditional 
#  statements (if-elif) evaluate each guess—providing feedback on whether it's too high, too low, 
#  or correct. If the guess matches, the loop breaks; otherwise, the game ends after 7 tries, 
#  displaying the correct number.

import random

print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!")

low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the Upper Bound: "))

print(f"\nYou have 7 chances to guess the number between {low} and {high}. Let's start!")

num = random.randint(low, high) 
ch = 7       # Total allowed chances
gc = 0       # Guess counter

while gc < ch:
    gc += 1
    guess = int(input('Enter your guess: '))

    if guess == num:
        print(f'Correct! The number is {num}. You guessed it in {gc} attempts.')
        break

    elif gc >= ch and guess != num:
        print(f'orry! The number was {num}. Better luck next time.')

    elif guess > num:
        print('Too high! Try a lower number.')

    elif guess < num:
        print('Too low! Try a higher number.')

        # out put will be
      
      
Enter Lower bound:-0
Enter Upper Bound: 100
You've only 7 chances to guess the integer! 
Guess a number:-45
You guessed too small! 
Guess a number:-78
You Guessed too high! 
Guess a number:-59
You Guessed too high! 
Guess a number:-57
You Guessed too high! 
Guess a number:-42
You guessed too small! 
Guess a number:-54
Congratulations you did it in 6 try 