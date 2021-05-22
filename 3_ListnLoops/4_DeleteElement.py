meat_list = ["Beef", "Goat", "Sheep", "Chicken", "Duck"]

print("Which meat do you want to delete from today's menu?\n" + str(meat_list))

meat_omit = int(input("Please select a number from -5 to 4: "))

del meat_list[meat_omit]

print("Your new meat menu is\n" + str(meat_list))
