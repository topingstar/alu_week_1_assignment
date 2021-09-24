trials = 6
tally = 0
correct = 0

print("Welcome to Q&A ALU Hangman!")

# question one
answer = input("\nWhen was ALU founded? ")

# a condition to check if the answer is correct
if answer == "2015":
    print("Correct!")
    # increases user's chances (tally) if he/she gets it correct
    tally += 1

# hangs the man if the user gets the answer wrong
else:
    print("You hanged the man!")

    # deducts the user's chances to play
    trials = trials - 1

    # checks if the user has depleted all the chances given and stops the game
    if trials == 0:
        print("You have depleted all of your chances!")
        print("\t\nTry again later")
        quit()

# follows the same order till the last question.
# question two

answer = input("\nWho is the CEO of ALU? ")
if answer == "Fred Swaniker":

    print("Correct!")
    tally += 1

else:
    print("You hanged the man!")

    trials = trials - 1

    if trials == 0:
        print("You have depleted all of your chances!")
        print("\t\nTry again later")
        quit()

# Question three
answer = input("\nWhere are ALU campuses? ")
if answer == "Rwanda and Mauritius" or answer == "Mauritius and Rwanda":

    print("Correct!")
    tally += 1

else:
    print("You hanged the man!")

    trials = trials - 1

    if trials == 0:
        print("You have depleted all of your chances!")
        print("\t\nTry again later")
        quit()

# Question four
answer = input("\nHow many campuses does ALU have? ")
if answer == "2":

    print("Correct!")
    tally += 1

else:
    print("You hanged the man!")

    trials = trials - 1

    if trials == 0:
        print("You have depleted all of your chances!")
        print("\t\nTry again later")
        quit()

# question five
answer = input("\nWhat is the name of ALU Rwanda’s Dean? ")
if answer == "Gaidi Faraj":

    print("Correct!")
    tally += 1

else:
    print("You hanged the man!")

    trials = trials - 1

    if trials == 0:
        print("You have depleted all of your chances!")
        print("\t\nTry again later")
        quit()

# question six
answer = input("\nWho is in charge of Student Life? ")
if answer == "Sila Ogidi":

    print("Correct!")
    tally += 1

else:
    print("You hanged the man!")

    trials = trials - 1

    if trials == 0:
        print("You have depleted all of your chances!")
        print("\t\nTry again later")
        quit()

# question seven
answer = input("\nWhat is the name of our Lab? ")
if answer == "Nigeria Lab" or answer == "Nigeria":

    print("Correct!")
    tally += 1

else:
    print("You hanged the man!")

    trials = trials - 1

    if trials == 0:
        print("You have depleted all of your chances!")
        print("\t\nTry again later")
        quit()

# question eight
answer = input("\nHow many students do we have in Year 2 CS? ")
if answer == "96":

    print("Correct!")
    tally += 1

else:
    print("You hanged the man!")

    trials = trials - 1

    if trials == 0:
        print("You have depleted all of your chances!")
        print("\t\nTry again later")
        quit()

# question nine
answer = input("\nHow many degrees does ALU offer ? ")
if answer == "8":

    print("Correct!")
    tally += 1

else:
    print("You hanged the man!")

    trials = trials - 1

    if trials == 0:
        print("You have depleted all of your chances!")
        print("\t\nTry again later")
        quit()

# question ten
answer = input("\nWhere are the headquarters of ALU? ")
if answer == "Mauritius":

    print("Correct!")
    tally += 1

else:
    print("You hanged the man!")

    trials = trials - 1

    if trials == 0:
        print("You have depleted all of your chances!")
        print("\t\nTry again later")
        quit()