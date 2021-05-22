stockholm_university = {'Location': 'Stockholm', 'Established': '1832', 'Total Students': '20000',
                        'World Ranking': '115'}

print("This is the details of Stockholm University \n" + str(stockholm_university))
print("Do you want to delete any details here?")
details = input("Y or N :").upper()

if details == "Y":
    key_title = input("Enter Key Title: ").title()
    if key_title == 'Location' or key_title == 'Established' or key_title == 'Total Students' or key_title == 'World Ranking':
        del stockholm_university[key_title]
        print("New details of Stockholm University -\n" + str(stockholm_university))
    else:
        print("Please enter the correct Key Title")
else:
    print("Thank you for agreeing with us!")
