# In plain English and with the Given-required-algorithm table,
# write a guessing game where the user should guess a secret number.
# After every guess, the program tells the user whether their number was too large or too small.
# In the end, the number of tries needed should be printed.

# Given
# Plain English
# Guessing game
# User to guess a secrete number

# Required
# Tell the user whether the number they guessed was too large or too small
# When guessed correctly, tell the user the number of tries needed to be printed

# Algorithm
# Import a random library to all the user to choose a random number
# import random
# create variable and echo to random.randrange (50, 100)
# number = random.randrange(50, 100)
# create a variable called guess and guesses that will enable the user to guess a number between 50 and 100
# guess = int(input("Guess a number between 50 and 100: "))
# guesses = 1

# use a while, if and else statements (loop) so that when the user has gotten the guessed number wrongly
# he/she will have to continue guessing until the user guesses the correct number and the game will stop
# while guess != number:
# if the user guesses the number that it is too small
# if guess < number:
# print("Your guess was too small. Try guessing again!")
# guess = int(input("\nGuess a number between 50 and 100: "))
# guesses = guesses + 1
# if the user guesses a number that is too large
# else:
# print("Your guess was too large. Try guessing again!")
# guess = int(input("\nGuess a number between 50 and 100: "))
# number_of_guesses = guesses + 1
# if user guessed the correct number
# print("Congrats! You guessed the correct number")
# shows the user the number of times he/she guessed
# print("It only took you", guesses, "guesses", "to get the right number")
