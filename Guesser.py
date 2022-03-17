# Creating the game "Guesser" where your goal is to guess the randomly selected number; 16.06.2017; Made on Python 3.6

# Adding imports
import random

# Introduction + username input
print("You are currently playing Guesser made on Python!")
uname = input("Hello stranger, what is your name? ")
print("Hello " + uname)

# Checking if the user would like to begin the game + if the user inputted correct information
answer_play = input("Want to play a game?[Y/N] ")
answer_play_low = answer_play.lower()

# Variable for the replay loops
replay = True

while replay == True:
    # Random number generation
    number = random.randint(1, 100)

    # For debugging purposes only
    # number = 50

    # Setting number of guesses
    number_of_guesses = 1

    # Variables for loops
    found = False
    repeat = True
    second_loop = True

    # Setting up the user answer loop
    while repeat == True:
        answer_play_low = answer_play.lower()
        if answer_play_low == "yes" or answer_play_low == "y":
            repeat = False

            # Setting the guessing process + counting the number of guesses
            guess = int(input("Ok then, lets begin! I'm thinking of a number between 1 and 100. Your job is to guess it! Go ahead and have a guess: "))
            while found == False:
                if guess == number:
                    print("Congratulations " + uname + ", You won!")
                    print("The number was: ", number)
                    found = True
                    print("It took you ", number_of_guesses, " guesses.")
                elif guess > number:
                    guess = int(input("Guess lower: "))
                    number_of_guesses += 1
                else:
                    guess = int(input("Guess higher: "))
                    number_of_guesses += 1
            # End of guessing process + number counting setup

            # Setting up the replay mechanism
            u_input = input("Would you like to play again?[Y/N] ")
            while second_loop == True:
                u_input_low = u_input.lower()
                if u_input_low == "y" or u_input_low == "yes":
                    second_loop = False
                    replay = True
                elif u_input_low == "n" or u_input_low == "no":
                    second_loop = False
                    replay = False
                    print("Thanks for playing!")
                else:
                    u_input = input("I did not understand that. Try again: ")
            # End of replay mechanism settup

        elif answer_play_low == "no" or answer_play_low == "n":
            repeat = False
            replay = False
            print("Ok, bye...")
        else:
            answer_play = input("I did not understand that. Try again: ")
