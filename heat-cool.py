# displays whether to turn the A/C up, down, or be put on standby
def heating_cooling(actual_temp, desired_temp):
    if actual_temp > desired_temp:
        print("Run A/C")
    elif actual_temp < desired_temp:
        print("Run heat")
    else:
        print("Standby")


# user choice is matched with the specific conversion value
def convert_temp(temp_celsius, target_unit):
    while True:

        match target_unit:
            case "K":
                return f"{(temp_celsius - 32) * (5 / 9) + 273.15:.1f} K"
            case "C":
                return f"{(temp_celsius - 32) * (5 / 9):.1f} C"
            case "F":
                return f"{temp_celsius} F"
            case _:
                target_unit = input("Please choose either C for Celsius, K for Kelvin, or F for Fahrenheit: ").upper()


# user chooses to break the loop or enter new values and start the program again
def loop_break():
    while True:
        x = input("Would you like to enter a new desired temperature?(Yes/No)\n").title()
        if x == "Yes":
            return True
        elif x == "No":
            return False
        else:
            print("Please answer with either yes or no only.\n")


# user chooses between Celsius, Kelvin, or Fahrenheit conversion
def user_type():
    while True:
        conversion = input("Would you like to convert desired temp to Celsius, Kelvin, or Fahrenheit?"
                           " (Yes/No)\n").lower()
        if conversion == "yes":
            conversion_choice = input("Please input C for Celsius, K for Kelvin, or F for Fahrenheit: ").upper()

            print(convert_temp(float(desired), conversion_choice))
            break
        elif conversion == "no":
            break
        else:
            print("Please choose one of the valid entries given.")


# test the A/C unit first by calling with different parameters
heating_cooling(75, 65)
heating_cooling(75, 80)

# gets what user wants to input and loops until they break out
loop = True
while loop:
    actual = input("Please enter the current temperature: ")
    desired = input("Please enter your desired temperature: ")

    heating_cooling(actual, desired)
    # asks user what scale they would like to use for temperature
    user_type()
    # loop breaking function
    loop = loop_break()
