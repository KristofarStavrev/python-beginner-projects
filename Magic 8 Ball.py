# Creating a Magic 8 Ball game on Python 3.6; 25.06.2017

# Adding imports
import random
import sys

# Creating the loop variable
replay = True

# Introduction + user input + checking if the user would like to begin the game + if the user inputted correct information
uname = input("Welcome to the wise magic 8 ball, stranger! Your name is: ")
print ("Hello, ", uname)
answer = input("Would you like to test the mighty knowledge of the magic 8 ball?[Y/N]: ")
answer_low = answer.lower()

# Creating the replay loop
while replay == True:

    # Creating variables for loops
    correct = True
    loop = True

    # Setting up the main mechanism of the game (The random AI choice + validating the the user inputted information)
    answer_low = answer.lower()
    random_number = random.randint(1, 8)
    # /for debugging only/ print (random_number)
    while correct == True:
        answer_low = answer.lower()
        if answer_low == "yes" or answer_low == "y":
            correct = False
            u_input = input("What would you like to ask?: ")
            if random_number == 1:
                print ("The magic 8 ball says: Yes definitely!")
            elif random_number == 2:
                print ("The magic 8 ball says: Signs point to yes.")
            elif random_number == 3:
                print ("The magic 8 ball says: Most likely.")
            elif random_number == 4:
                print ("The magic 8 ball says: Cannot predict now.")
            elif random_number == 5:
                print ("The magic 8 ball says: Ask agian later.")
            elif random_number == 6:
                print ("The magic 8 ball says: Don't count on it.")
            elif random_number == 7:
                print ("The magic 8 ball says: My sources say no.")
            else:
                print ("The magic 8 ball says: Very doubtful!")
        elif answer_low == "no" or answer_low == "n":
            correct = False
            print ("Ok... may we meet agian!")
            sys.exit(0)
        else:
            answer = input("I did not understand that. Try agian: ")

    # Asking for user input (replay mechanism setup)
    us_input = input("Would you like to ask another question?[Y/N] ")
    us_input_low = us_input.lower()
    while loop == True:
        us_input_low = us_input.lower()
        if us_input_low == "yes" or us_input_low == "y":
            replay = True
            loop = False
        elif us_input_low == "no" or us_input_low == "n":
            replay = False
            loop = False
            print ("Thanks for playing!")
        else:
            us_input = input("I did not understand that. Try agian: ")
