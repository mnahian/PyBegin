print("Let's calculate your Cineplex discount!")

cineplex_entry = int(input("How many times have you seen movies in cineplex? "))
ticket_price = 120
discount = [15, 30, 45, 60, 75]

if 25 <= cineplex_entry:
    print("Ticket price: US$ " + str(ticket_price) +
          "\nNumber of entry: " + str(cineplex_entry) +
          "\nQualify discount: US$ " + str(discount[4]) +
          "\nYour final ticket price US$ " + str(ticket_price-discount[4])
          )
elif 20 <= cineplex_entry <= 24:
    print("Ticket price: US$ " + str(ticket_price) +
          "\nNumber of entry: " + str(cineplex_entry) +
          "\nQualify discount: US$ " + str(discount[3]) +
          "\nYour final ticket price US$ " + str(ticket_price - discount[3])
          )
elif 15 <= cineplex_entry <= 19:
    print("Ticket price: US$ " + str(ticket_price) +
          "\nNumber of entry: " + str(cineplex_entry) +
          "\nQualify discount: US$ " + str(discount[2]) +
          "\nYour final ticket price US$ " + str(ticket_price - discount[2])
          )
elif 10 <= cineplex_entry <= 14:
    print("Ticket price: US$ " + str(ticket_price) +
          "\nNumber of entry: " + str(cineplex_entry) +
          "\nQualify discount: US$ " + str(discount[1]) +
          "\nYour final ticket price US$ " + str(ticket_price - discount[1])
          )
elif 5 <= cineplex_entry <= 9:
    print("Ticket price: US$ " + str(ticket_price) +
          "\nNumber of entry: " + str(cineplex_entry) +
          "\nQualify discount: US$ " + str(discount[0]) +
          "\nYour final ticket price US$ " + str(ticket_price - discount[0])
          )
else:
    print("Sorry, you don't qualify for any discount.")