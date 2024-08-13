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
                print("Please choose either C for Celsius, K for Kelvin, or F for Fahrenheit")


# user chooses to break the loop or enter new values and start the program again
def loop_break():
    while True:
        x = input("Would you like to enter new values?(Yes/No)\n").title()
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
                           " (yes/no)\n").lower()
        if conversion == "yes":
            conversion_choice = input("Please input C for Celsius, K for Kelvin, or F for Fahrenheit: ").upper()

            print(convert_temp(float(desired), conversion_choice))
            break
        else:
            print("Please choose one of the valid entries given.")


loop = True
while loop:
    actual = input("Please enter the current temperature: ")
    desired = input("Please enter your desired temperature: ")

    heating_cooling(actual, desired)
    user_type()
    loop = loop_break()
