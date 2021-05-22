multi_cultural_pizza = ["Veggie Supreme", "Double Cheese", "Spicy Beef", "Spicy Chicken",
         "BBQ Temptation", "Chicken Hawaiian", "Beef Pepperoni", "Meat Lovers"]

print("\n" + "We have a family size Multi-Cultural/Multi Toppings Pizza -")
for List in multi_cultural_pizza:
    print(List)

print("\n" + "Please choose your slice by entering number 0 to 8 below and start number has to be smaller than the end number -")
start_slice = int(input("Start Number: "))
end_slice = int(input("End Number: "))

print("You have chosen the follwoing slices - \n" + str(multi_cultural_pizza[start_slice:end_slice]))