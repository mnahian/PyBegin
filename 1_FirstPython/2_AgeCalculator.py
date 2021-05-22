print("Please answer the question to calculate your life span!")
name =  input("Name: ")
print("What is your age? ", (name), "?")
age = int(input("Age: "))
days = age * 365
minutes = age * 525948
seconds = age * 31556926

print(name, " has been lived for ", days, "  days", minutes, " minutes", seconds, " seconds")
print("Thank you for using my age calculator!")