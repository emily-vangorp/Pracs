from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0
    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != 'q':
        if menu_choice == 'c':
            print("Taxis available:")
            for index, taxi_details in enumerate(taxis):
                print("{} - {}".format(index, taxi_details))
            chosen_taxi = int(input("Choose taxi: "))
            print("Bill to date: ${:.2f}".format(bill_to_date))
        elif menu_choice == 'd':
            distance = int(input("Drive how far? "))

        print(MENU)
        menu_choice = input(">>> ").lower()


main()
