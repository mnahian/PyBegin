cricket_nation = ["Australia", "Bangladesh", "Pakistan", "India",
                  "Sri Lanka", "England", "South Africa", "West Indies",
                  "New Zealand", "Zimbabwe", "Afganistan"]

print("Please enter the country name to check if it is test playing nation or not")
check_nation = input("Country Name: ").title()

if check_nation in cricket_nation:
    print("Yes! " + check_nation + " is a test playing nation!")
else:
    print("No, " + check_nation + " is not a test playing nation.")