# Number Guessing Game
This is a simple Python command-line game where the player tries to guess a randomly generated number 
within a specified range. The player has 7 chances to guess the correct number.

How to Play

When you run the script, you will be greeted with a welcome message.
Enter the lower and upper bounds for the number range.
The program will randomly select a number within your specified range.
You have 7 attempts to guess the number.
After each guess, you'll receive feedback:
"Too high! Try a lower number." if your guess is above the target.
"Too low! Try a higher number." if your guess is below the target.
"Correct! The number is X. You guessed it in Y attempts." if you guess correctly.
If you fail to guess within 7 attempts, the correct number is revealed.

Example Output

Code

Hi! Welcome to the Number Guessing Game.
You have 7 chances to guess the number. Let's start!
Enter the Lower Bound: 0
Enter the Upper Bound: 100

You have 7 chances to guess the number between 0 and 100. Let's start!
Enter your guess: 45
Too low! Try a higher number.
Enter your guess: 78
Too high! Try a lower number.
Enter your guess: 59
Too high! Try a lower number.
Enter your guess: 57
Too high! Try a lower number.
Enter your guess: 42
Too low! Try a higher number.
Enter your guess: 54
Correct! The number is 54. You guessed it in 6 attempts.
Requirements
Python 3.x
How to Run
Save the script as games.py.
Open a terminal and navigate to the script's directory.
Run the script with:
Code
python games.py

Notes

The game uses Python's built-in random module to generate the number.
Make sure to enter valid integer values for the lower and upper bounds.