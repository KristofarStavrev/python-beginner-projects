# Creating a unit convert; 01.08.2017; Made on Python 3.5.3

# Introduction
print("Unit converter made with python 3.5.3")

# Defining the main function


def converter():

    print("""type:
    1 for temperature unit converter
    2 for lenght unit converter
    3 for velocity unit converter (speed)
    4 for weight/mass unit converter
    5 for volume unit converter
    """)
    uselect = input("What would you like to convert? ")

    # variables
    check = True
    check1 = True
    check2 = True
    check3 = True
    check4 = True
    check5 = True

    while check == True:

        if uselect == "1":
            check = False
            temp_input = input("""
            (1)Fahrenheit to Celsius
            (2)Celsius to Fahrenheit
            input: """)
            while check1 == True:
                if temp_input == "1":
                    check1 = False
                    fahrenheit_input = input("Fahrenheit degrees: ")
                    while True:
                        try:
                            fahrenheit_input_int = int(fahrenheit_input)
                            break
                        except ValueError:
                            fahrenheit_input = input("Invalid input. Try again: ")
                    celsius = (((fahrenheit_input_int - 32) * 5) / 9)
                    print("{0} degrees Fahrenheit equal to {1} degrees Celsius".format(fahrenheit_input_int, celsius))
                elif temp_input == "2":
                    check1 = False
                    celsius_input = input("Celsius: ")
                    while True:
                        try:
                            celsius_input_int = int(celsius_input)
                            break
                        except ValueError:
                            celsius_input = input("Invalid input. Try again: ")
                    fahrenheit = (((celsius_input_int * 9) / 5) + 32)
                    print("{0} degrees Celsius equal to {1} degrees Fahrenheit".format(celsius_input_int, fahrenheit))
                else:
                    temp_input = input("Invalid input. Try again: ")

        elif uselect == "2":
            check = False
            lenght_input = input("""
            (1)Miles to Kilometers
            (2)Kilometers to Miles
            (3)Inches to Centimeters
            (4)Centimeters to Inches
            (5)Meters to Feet
            (6)Feet to Meters
            input: """)
            while check2 == True:
                if lenght_input == "1":
                    check2 = False
                    miles_input = input("Miles: ")
                    while True:
                        try:
                            miles_input_int = int(miles_input)
                            break
                        except ValueError:
                            miles_input = input("Invalid input. Try again: ")
                    km = miles_input_int * 1.609344
                    print("{0} Miles equal to {1} Kilometers".format(miles_input_int, km))
                elif lenght_input == "2":
                    check2 = False
                    km_input = input("Kilometers: ")
                    while True:
                        try:
                            km_input_int = int(km_input)
                            break
                        except ValueError:
                            km_input = input("Invalid input. Try again: ")
                    miles = km_input_int * 0.621371
                    print("{0} Kilometers equal to {1} Miles".format(km_input_int, miles))
                elif lenght_input == "3":
                    check2 = False
                    print("3")
                elif lenght_input == "4":
                    check2 = False
                    print("4")
                elif lenght_input == "5":
                    check2 = False
                    print("5")
                elif lenght_input == "6":
                    check2 = False
                    print("6")
                else:
                    lenght_input = input("Invalid input. Try again: ")

        elif uselect == "3":
            check = False
            speed_input = input("""
            (1)Miles per hour Mp/h to Kilometers per hour Km/h
            (2)Kilometers per hour Km/h to Miles per hour Mp/h
            input: """)
            while check3 == True:
                if speed_input == "1":
                    check3 = False
                    print("1")
                elif speed_input == "2":
                    check3 = False
                    print("2")
                else:
                    speed_input = input("Invalid input. Try again: ")

        elif uselect == "4":
            check = False
            mass_input = input("""
            (1)Pounds to Kilograms
            (2)Kilograms to Pounds
            input: """)
            while check4 == True:
                if mass_input == "1":
                    check4 = False
                    print("1")
                elif mass_input == "2":
                    check4 = False
                    print("2")
                else:
                    mass_input = input("Invalid input. Try again: ")

        elif uselect == "5":
            check = False
            volume_input = input("""
            (1)Pints (US) to Litres
            (2)Litres to Pints (US)
            (3)Gallons (US) to Litres
            (4)Litres to Gallons (US)
            input: """)
            while check5 == True:
                if volume_input == "1":
                    check5 = False
                    print("1")
                elif volume_input == "2":
                    check5 = False
                    print("2")
                elif volume_input == "3":
                    check5 = False
                    print("3")
                elif volume_input == "4":
                    check5 = False
                    print("4")
                else:
                    volume_input = input("Invalid input. Try again: ")

        else:
            uselect = input("Invalid input. Try again: ")

# Calling the converter function


converter()

# Creating a loop that recalls the main converter function
while True:
    ask = input("Would you like to convert something else?[Y/N]: ")
    ask_low = ask.lower()
    if ask_low == "y" or ask_low == "yes":
        converter()
    elif ask_low == "n" or ask_low == "no":
        break
