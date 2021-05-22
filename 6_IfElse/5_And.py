covit_vaccine = int(input("Your Age? "))

if covit_vaccine >= 0 and covit_vaccine <=17:
    print("You are not eligible for Covit Vaccine.")
elif covit_vaccine >= 18 and covit_vaccine <=64:
    print("You are eligible for Covit Vaccine!")
elif covit_vaccine >=65 and covit_vaccine <=99:
    print("You are eligible for Covit Tablet.")
else:
    print("You age can't be " + str(covit_vaccine) + "! Please enter the correct age.")
