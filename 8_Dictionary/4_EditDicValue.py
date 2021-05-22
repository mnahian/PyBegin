stockholm_university = {'Location': 'Stockholm', 'Established': '1832', 'Total Students': '20000',
                        'World Ranking': '115'}

print("This is the details of Stockholm University \n" + str(stockholm_university))
print("Do you want to update any details here?")
details = input("Y or N :").upper()

if details == "Y":
    key_title = input("Enter Key Title: ").title()
    key_value = input("Enter Key Value: ").title()
    stockholm_university[key_title] = key_value
    print("New details of Stockholm University -\n" + str(stockholm_university))
else:
    print("Thank you for agreeing with us!")
