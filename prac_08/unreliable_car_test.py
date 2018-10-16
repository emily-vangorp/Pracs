from prac_08.unreliable_car import UnreliableCar


def main():
    bad_car = UnreliableCar("Vinnie", 100, 50)
    bad_car.drive(40)
    print(bad_car)


main()
