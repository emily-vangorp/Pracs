"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Car", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("{} {}, {}".format(my_car.name, my_car.fuel, my_car.odometer))
    print("{} {self.fuel}, {self.odometer}".format(my_car.name, self=my_car))

    my_car = Car("Limo", 100)
    my_car.add_fuel(20)
    print("{} has {} units of fuel".format(my_car.name, my_car.fuel))
    my_car.drive(115)
    print("{}'s odometer is {}".format(my_car.name, my_car.odometer))


main()

