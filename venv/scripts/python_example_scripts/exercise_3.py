# Write a Python program to guess a number between 1 to 9. Go to the editor
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again
# until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.
# author Jaba
import random

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Enter Guess:"))  # ask user for a value
    guess_count += 1  # increment the count every time a guess is made

    if guess == secret_number:
        print("You Just Won")
        break  # breaks the loop there right value has been guessed
else:
    print("You Failed Try Again!!!")
