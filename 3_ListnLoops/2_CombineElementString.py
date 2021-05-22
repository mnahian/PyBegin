f_celebrity = ["Mila Kunis", "Amanda Seyfried", "Hayden Panettiere",
               "Missy Peregrym", "Rachel McAdams", "Shantel VanSanten",
               "Natalie Portman", "Black Swan", "Sophia Bush",
               "Malin Akerman", "Michelle Monaghan", "Jennifer Connelly"]

name = input("Your name: ").title()

print(name, "select a number between -11 to 10 to find out the celebrity who fancies you most!")

love = int(input("Number: "))

print(name+ ", " + f_celebrity[love] + " has serious crash on you!!")
