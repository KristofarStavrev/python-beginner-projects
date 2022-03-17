# Creating the game "Gamblr" where your goal is to guess if the next number will be higher or lower than the previous one; Christopher Stavrev; 04.07.2017; Made on Python 3.6

# Adding imports
import random

# Defining the variables
starting_number = random.randint(1, 100)
checking = True
coins = 10
repeat_first = True
repeat_game = True
have = True
bet = 0
jackpot = False
jackpot_setup = False
once = False

# Introduction + user input (name; begin game)
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~rules~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
uname = input("""Hello and welcome to the Gamblr! The rules of the game are simple - your goal is to guess if the next number is going to be bigger or smaller than the previous one.
The numbers range frong 1 to 100. You also have to option to choose how many coins to bet on a roll. The payout is 1:1 which means that for example if you bet 5 coins and win
you get to keep your initial bet (5 coins) and get an additional 5 more coins. You begin with 10 coins and can place the following bets
[1][2][5][10][25][50][100][1,000][10,000(Jackpot!)] coins. You can use 'b' for bigger or 's' for smaller. You can quit at any time by typing 'q' or 'quit'. Please input your name: """)
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~rules~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
begin = input("So, " + uname + " would you like to begin your adventures in the gambling world?[Y/N] ")
begin_low = begin.lower()

# Game loop
while checking == True:
    begin_low = begin.lower()
    if begin_low == "y" or begin_low == "yes":
        checking = False

        # Setting up the loop for the bet + coin displaying + special situations (0 coins; 10,000 coins)
        while repeat_game == True:
            have = True
            print ("You have {0} coins".format(coins))

            if coins == 0:
                print ("You don't have any coins. You are broke! Come back when you have more money.")
                break

            if coins >= 10000 and coins <= 11000 and once == False:
                print ("""Congratulations you managed to grind all the way to 10 grand!. If you decide to bet 10,000 coins (this is as we call it 'The big play') and win
                you get to walk out with 1,000,000 coins!""")
                jackpot_setup = True

            money = input("Your bet: ")

            # Quit function
            if money == "quit" or money == "q" or money == "Quit" or money == "Q" or money == "QUIT":
                print ("See you soon.")
                break

            # A loop that checks if the user input is valid (integer)
            while True:
                try:
                   money_int = int(money)
                   break
                except ValueError:
                    money = input("Invalid input. Try again: ")

            # Loop that checks if the bet input is correct
            while have == True:
                have = True
                money_int = int(money)
                if money_int <= coins and money_int == 1:
                    have = False
                    bet = 1
                elif money_int <= coins and money_int == 2:
                    have = False
                    bet = 2
                elif money_int <= coins and money_int == 5:
                    have = False
                    bet = 5
                elif money_int <= coins and money_int == 10:
                    have = False
                    bet = 10
                elif money_int <= coins and money_int == 25:
                    have = False
                    bet = 25
                elif money_int <= coins and money_int == 50:
                    have = False
                    bet = 50
                elif money_int <= coins and money_int == 100:
                    have = False
                    bet = 100
                elif money_int <= coins and money_int == 1000:
                    have = False
                    bet = 1000
                elif money_int <= coins and money_int == 10000 and jackpot_setup == True:
                    have = False
                    bet = 10000
                    jackpot_setup = False
                    jackpot = True
                elif money_int <= coins and money_int == 10000:
                    have = False
                    bet = 10000
                else:
                    money = input ("Invalid input. Try again: ")
                    continue

                # Setting up tha random mechanism + the user guess
                next_number = random.randint(1, 100)
                print ("The previous number was: ", starting_number)
                uguess = input("The next number is going to be [b/s]")
                uguess_low = uguess.lower()
                repeat_first = True

                # Game logic that checks if the player wins or loses + quit function
                while repeat_first == True:
                    uguess_low = uguess.lower()
                    if starting_number > next_number:
                        win_condition = "smaller"
                    elif starting_number < next_number:
                        win_condition = "bigger"
                    else:
                        win_condition = "same"

                    if uguess_low == "b" and win_condition == "smaller":
                        print ("You lose! The number was ", next_number, " which is smaller than the previous number.")
                        repeat_first = False
                        starting_number = next_number
                        coins = coins - bet
                    elif uguess_low == "s" and win_condition == "smaller":
                        print ("You win! The number was ", next_number, " which is smaller than the previous number.")
                        repeat_first = False
                        starting_number = next_number
                        if jackpot == True:
                            coins = 1000000
                            print ("JACKPOT")
                            jackpot = False
                            once = True
                        else:
                            coins = coins + bet
                    elif uguess_low == "b" and win_condition == "bigger":
                        print ("You win! The number was ", next_number, " which is bigger than the previous number.")
                        repeat_first = False
                        starting_number = next_number
                        if jackpot == True:
                            coins = 1000000
                            print ("JACKPOT")
                            jackpot = False
                            once = True
                        else:
                            coins = coins + bet
                    elif uguess_low == "s" and win_condition == "bigger":
                        print ("You lose! The number was ", next_number, " which is bigger than the previous number.")
                        repeat_first = False
                        starting_number = next_number
                        coins = coins - bet
                    elif (uguess_low == "s" or uguess_low == "b") and win_condition =="same":
                        print ("The next number was the same as the previous number... now thats lucky.")
                        repeat_first = False
                        starting_number = next_number
                    elif uguess_low == "quit" or uguess_low == "q":
                        repeat_first = False
                        repeat_game = False
                        print ("See you soon.")
                    else:
                        uguess = input("Incorrect input. Please try again: ")

    elif begin_low == "n" or begin_low == "no":
        checking = False
        print ("Ok then, you miss...")
    else:
        begin = input("Invalid input. Try again: ")
