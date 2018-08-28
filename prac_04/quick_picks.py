import random

MIN_PICK = 1
MAX_PICK = 45

no_of_quick_picks = int(input("How many quick picks? "))
for i in range(no_of_quick_picks):
    numbers = []
    for k in range(6):
        number = random.randint(MIN_PICK, MAX_PICK)
        while number in numbers:
            number = random.randint(MIN_PICK, MAX_PICK)
        numbers.append(number)
    print(sorted(numbers))
