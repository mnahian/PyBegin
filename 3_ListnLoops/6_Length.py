animals = ["Sydney Spider", "Black Mamba", "Puffer Fish",
           "Indian Viper", "Box Jellyfish", "Golden Frog",
           "Cone Snail", "Cape Buffalo"]

print("This is the animal list \n", animals, "\n")

print("Do you want to know how many elements are in this list?"
      "\n y or n")

reply = input("Your answer: ")

if reply == "y":
    print("\n There are", len(animals), "elements in the list")
else:
    print("\n you can count it by yourself then!")


