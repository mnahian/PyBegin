i = 1
new_wife = ""

while i <= 1:
    wife_name = input("What is your wife name? ").title()
    wife_age = input("What is your wife age? ").title()
    wife_nationality = input("What is your wife's nationality? ").title()


    def name():
        print("Your wife name is " + wife_name)


    def age():
        print("Your wife age is " + wife_age)


    def nationality():
        print("Your wife's nationality is " + wife_nationality)


    name()
    age()
    nationality()

    new_wife = input("\nDo you want to continue? Y or N: ").upper()
    if new_wife == "Y":
        print("\nPlease enter your wife's details below -")
    else:
        i += 1
        print("The program has ended now!")

