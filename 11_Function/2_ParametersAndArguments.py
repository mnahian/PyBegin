# defining the function with parameters
def wife(wife_name, wife_age):
    print("My wife name is " + wife_name + " and her age is " + str(wife_age))


# defining the arguments
wife_name = input("Your wife name: ").title()
wife_age = input("Your wife age: ").title()

wife(wife_name,wife_age)