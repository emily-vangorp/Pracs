sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print("Bonus: $" + str(bonus) + "0")
    sales = float(input("Enter sales: $"))
