from prac_06.guitar import Guitar


# my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
# another_guitar = Guitar("Another Guitar", 2012, 6050.95)
# print("{} get_age() - Expected 96. Got {}".format(my_guitar.name, my_guitar.get_age()))
# print("{} get_age() - Expected 6. Got {}".format(another_guitar.name, another_guitar.get_age()))
# print("{} is_vintage() - Expected True. Got {}".format(my_guitar.name, my_guitar.is_vintage()))
# print("{} is_vintage() - Expected False. Got {}".format(another_guitar.name, another_guitar.is_vintage()))

def main():
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Another Guitar", 2012, 6050.95))

    guitars.sort()
    print("These are my guitars:")

    if guitars is not None:
        for i, guitar in enumerate(guitars):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print("Guitar {0}: {1.name:>30} ({1.year}), worth ${1.cost:10,.2f}\
                  {2}".format(i + 1, guitar, vintage_string))
    else:
        print("No guitars :( Quick go and buy one!")


main()
