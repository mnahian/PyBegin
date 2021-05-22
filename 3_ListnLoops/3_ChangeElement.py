natural_beauties = ["Bangladesh", "New Zealand", "Sweden", "USA", "UK", "Saudi Arabia"]

print("According to us the most beautiful countries are:\n" + str(natural_beauties))

country_no = int(input("Please choose a value from -6 to 5: "))
new_country = input("What is your new country? ")

natural_beauties[country_no] = new_country.title()

print("Your new country list is \n" + str(natural_beauties))
