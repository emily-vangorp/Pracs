from prac_06.guitar import Guitar

my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2012, 6050.95)
# print("{} get_age() - Expected 96. Got {}".format(my_guitar.name, my_guitar.get_age()))
# print("{} get_age() - Expected 6. Got {}".format(another_guitar.name, another_guitar.get_age()))
# print("{} is_vintage() - Expected True. Got {}".format(my_guitar.name, my_guitar.is_vintage()))
# print("{} is_vintage() - Expected False. Got {}".format(another_guitar.name, another_guitar.is_vintage()))

print("My guitars!")
guitar = Guitar
guitars = []
while guitar.name != "":
    guitar.name = input("Name: ")
    guitar.year = int(input("Year: "))
    guitar.cost = float(input("Cost: $"))
    print("{} ({}) : ${} added.".format(guitar.name, guitar.year, guitar.cost))
    guitars.append(guitar)
print(guitars)

