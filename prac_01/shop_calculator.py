total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    print("Must have at least 1 item.")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    item_price = float(input("Price of item: "))
    total_price += item_price
print("Total price for", number_of_items, "items is $" + str(total_price) + "0")
