first_name = ""
last_name = ""


def apple_ceo(first_name="Mehedi", last_name="Nahian"):
    print("The CEO of Apple is: " + first_name + " " + last_name)


apple_ceo()

apple_ceo_name_change = input("Do you want to change the apple CEO name? Y or N: ").upper()

if apple_ceo_name_change == "Y":
    first_name = input("First Name: ").title()
    last_name = input("Last Name: ").title()
    apple_ceo(first_name, last_name)
else:
    print("Program is ended!")
