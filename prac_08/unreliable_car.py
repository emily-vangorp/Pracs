from prac_08.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.name = name
        self.fuel = fuel
        self.reliability = reliability

    def drive(self, distance):
        reliability_random = random.randint(0, 100)
        if reliability_random < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            print("Car didn't start")
            distance_driven = 0
            return distance_driven
