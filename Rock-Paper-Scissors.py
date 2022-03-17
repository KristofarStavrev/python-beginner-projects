# Creating a basic rock, paper, scissors game on Python 3.6; 18.06.2017

# Adding imports
import random

# Setting varibles (including replayability loop)
game_loop = True
player_wins = 0
bot_wins = 0
ties = 0

# Asking if the user wants to begin the game + introduction
print ("You are currently playing Guesser made on Python!")
answer = input("Hello, would you like to play a game of rock, paper, scissors?[Y/N] ")
answer_low = answer.lower()

# Setting up the replay loop
while game_loop == True:

    # Setting up the random number + the random selection between rock, paper or scissors
    random_num = random.randint(1, 3)
    if random_num == 1:
        ai_variable = "Rock"
    elif random_num == 2:
        ai_variable = "Paper"
    else:
        ai_variable = "Scissors"
    # /Used only for debugging/ print (ai_variable)

    # Setting up variables for loops
    repeat = True
    selection_loop = True
    second_loop = True

    # Setting up the user answer loop
    while repeat == True:
        answer_low = answer.lower()
        if answer_low == "yes" or answer_low == "y":
            repeat = False

            # Setting up the user selection between rock, paper or scissors
            # Comparing the user selection with the AI random selection
            # Setting up a loop in case the user input is invalid

            user_selection = input("Ok, so choose between rock, paper or scissors. You can use r, p or s for short or 1, 2, 3: ")
            user_selection_low = user_selection.lower()

            while selection_loop == True:
                user_selection_low = user_selection.lower()
                if (user_selection_low == "rock" or user_selection_low == "r" or user_selection_low == "1") and ai_variable == "Rock":
                    selection_loop = False
                    ties += 1
                    print ("You chose rock, the AI chose rock too so it's a tie!")
                elif (user_selection_low == "paper" or user_selection_low == "p" or user_selection_low == "2") and ai_variable == "Paper":
                    selection_loop = False
                    ties += 1
                    print ("You chose paper, the AI chose paper too so it's a tie!")
                elif (user_selection_low == "scissors" or user_selection_low == "s" or user_selection_low == "3") and ai_variable == "Scissors":
                    selection_loop = False
                    ties += 1
                    print ("You chose scissors, the Ai chose scissors too so it's a tie!")
                elif (user_selection_low == "rock" or user_selection_low == "r" or user_selection_low == "1") and ai_variable == "Paper":
                    selection_loop = False
                    bot_wins += 1
                    print ("You chose rock, the AI chose paper so you lose!")
                elif (user_selection_low == "rock" or user_selection_low == "r" or user_selection_low == "1") and ai_variable == "Scissors":
                    selection_loop = False
                    player_wins += 1
                    print ("You chose rock, the AI chose scissors so you win!")
                elif (user_selection_low == "paper" or user_selection_low == "p" or user_selection_low == "2") and ai_variable == "Rock":
                    selection_loop = False
                    player_wins += 1
                    print ("You chose paper, the AI chose rock so you win!")
                elif (user_selection_low == "paper" or user_selection_low == "p" or user_selection_low == "2") and ai_variable == "Scissors":
                    selection_loop = False
                    bot_wins += 1
                    print ("You chose paper, the AI chose scissors so you lose!")
                elif (user_selection_low == "scissors" or user_selection_low == "s" or user_selection_low == "3") and ai_variable == "Paper":
                    selection_loop = False
                    player_wins += 1
                    print ("You chose scissors, the AI chose paper so you win!")
                elif (user_selection_low == "scissors" or user_selection_low == "s" or user_selection_low == "3") and ai_variable == "Rock":
                    selection_loop = False
                    bot_wins += 1
                    print ("You chose scissors, the AI chose rock so you lose!")
                else:
                    user_selection = input("I did not understand that. Try again: ")

            # End of user selection process
            # End of comparison
            # End of loop setup

            # Setting up the replay mechanism
            print ("Your wins = ", player_wins)
            print ("Losses = ", bot_wins)
            print ("Ties = ", ties)
            retry = input("Would you like to play again?[Y/N] ")
            while second_loop == True:
                retry_low = retry.lower()
                if retry_low == "yes" or retry_low == "y":
                    game_loop = True
                    second_loop = False
                elif retry_low == "no" or retry_low == "n":
                    game_loop = False
                    second_loop = False
                    print ("Thanks for playing!")
                else:
                    retry = input("I did not understand that. Try again: ")

            # End of replay mechachism setup

        elif answer_low == "no" or answer_low == "n":
            repeat = False
            game_loop = False
            print ("Oh, ok bye then...")
        else:
            answer = input("I did not understand that. Try again: ")
