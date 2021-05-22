print("Do you have hair?")
hair = input("y or n: ").lower()
if hair == "y":
    print("You are lucky to have hair but maintaining hair is expensive!")
elif hair == "n":
    print("Although, you don't have any hair yet it saves money for you!")
else:
    print("Don't be naughty! Enter either y or n to get a answer!")