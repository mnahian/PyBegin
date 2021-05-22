donations = [15,12,17,7,74,34,98,49,15,3,459,761]
print("These are the donations we have got so far -")
for List in donations:
    print("USD $" + str(List))

print("\n Type 1 to find out the lowest donation"
    + "\n Type 2 to find out the highest donation"
    + "\n Type 3 to find out the total donation")

number = int(input("Number: "))

if number == 1:
    print("The lowest donation is USD $" + str(min(donations)))
elif number == 2:
    print("The highest donation is USD $" + str(max(donations)))
elif number == 3:
    print("The total donations is USD $" + str(sum(donations)))
else:
    print("Why are you not following the instructions?")
