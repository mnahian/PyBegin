print("Let's calculate your monthly car installment!")

name = input("Your Name: ").title()
salary = int(input("Your Salary: US$"))

monthly_installment = [50, 150, 450]

if 5000 <= salary <= 50000:
    print("Hello " + str(name) + ", based on your salary your monthly installment is US$" + str(monthly_installment[2]))
elif 2500 <= salary <= 4999:
    print("Hello " + str(name) + ", based on your salary your monthly installment is US$" + str(monthly_installment[1]))
elif 700 <= salary <= 2499:
    print("Hello " + str(name) + ", based on your salary your monthly installment is US$" + str(monthly_installment[0]))
else:
    print("Hello " + str(name) + ", the salary seems like an abnormal amount! We will give you a call.")
    cell_number = input("Your Cell Number: ")
    email_id = input("Your Email ID: ")
    print("Thank you " + str(name) + "! (Cell: " + str(cell_number) + " Email: "+ str(email_id) + ")")
    print("Expect a call from us in 3 working days!")