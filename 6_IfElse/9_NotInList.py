apple_products = ["iphone", "mac book pro", "ipad", "ipod", "mac pro"
                  "mac mini", "mac book air", "imac", "ipod classic",
                  "ipod nano", "ipad pro"]

print("Please type the product name to check if it's is apple product or not!")
product_name = input("Name: ").lower()

if product_name not in apple_products:
    print(product_name.title() + " is not an Apple product")
else:
    print(product_name.title() + " is an Apple product")