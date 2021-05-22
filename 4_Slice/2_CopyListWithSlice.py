cold_drinks = ["Mojo", "RC Cola", "Virgin Cola", "Merinda", "7 Up"]
updated_cold_drinks = cold_drinks[:]

print("These are the drinks you will get for next month -")
for List in cold_drinks:
    print(List)

print("Do you want to add any other drink?")
add_drink = input("y or n: ").lower()
if add_drink == "y":
    new_drink = input("New Drink Name: ").title()
    updated_cold_drinks.append(new_drink)
    print("Your new drink list is -")
    for List in updated_cold_drinks:
        print(List)
else:
    print("You didn't add any drink name, so the original list will be in place")