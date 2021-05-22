iphone_12_pro = {"Name": "iPhone 12 Pro", "Camera": "12mp", "Battery": "2815mAh", "RAM": "6GB"}

print("This is the specifications we have for iPhone 12 Pro!")
print(iphone_12_pro)
print("Description:", iphone_12_pro["Name"], iphone_12_pro["Camera"], iphone_12_pro["Battery"], iphone_12_pro["RAM"])

print("\nWould you like to add any more details?")
details = input("Y or N: ").upper()

if details == "Y":
    title = input("Title: ").title()
    description = input("Description: ").title()
    iphone_12_pro = {title: description}
    print(iphone_12_pro[title])
else:
    print("Have a nice day!")

