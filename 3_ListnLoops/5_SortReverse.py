dangerous_animals = ["Sydney Spider", "Black Mamba", "Puffer Fish",
                    "Indian Viper", "Box Jellyfish", "Golden Frog",
                    "Cone Snail", "Cape Buffalo"]

print("This is the normal list\n" + str(dangerous_animals))

dangerous_animals.reverse()
print("\n To reverse the list -"
      , "\n 1 ", str(dangerous_animals[0])
      , "\n 2 ", str(dangerous_animals[1])
      , "\n 3 ", str(dangerous_animals[2])
      , "\n 4 ", str(dangerous_animals[3])
      , "\n 5 ", str(dangerous_animals[4])
      , "\n 6 ", str(dangerous_animals[5])
      , "\n 7 ", str(dangerous_animals[6])
      , "\n 8 ", str(dangerous_animals[7])
      )

dangerous_animals.sort()
print("\n To sort the list alphabetically -"
      , "\n 1 ", str(dangerous_animals[0])
      , "\n 2 ", str(dangerous_animals[1])
      , "\n 3 ", str(dangerous_animals[2])
      , "\n 4 ", str(dangerous_animals[3])
      , "\n 5 ", str(dangerous_animals[4])
      , "\n 6 ", str(dangerous_animals[5])
      , "\n 7 ", str(dangerous_animals[6])
      , "\n 8 ", str(dangerous_animals[7])
      )

dangerous_animals.sort(reverse=True)
print("\n To sort the list reverse alphabetically -"
      , "\n 1 ", str(dangerous_animals[0])
      , "\n 2 ", str(dangerous_animals[1])
      , "\n 3 ", str(dangerous_animals[2])
      , "\n 4 ", str(dangerous_animals[3])
      , "\n 5 ", str(dangerous_animals[4])
      , "\n 6 ", str(dangerous_animals[5])
      , "\n 7 ", str(dangerous_animals[6])
      , "\n 8 ", str(dangerous_animals[7])
      )


