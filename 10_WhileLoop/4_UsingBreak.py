i = 1
user =""

while i <= 5:
    user = input("Name: ").title()
    if user == "John":
        break
    elif user == "Mic":
        continue
    i += 1
