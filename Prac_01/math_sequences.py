num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter another number: "))
print("(E)vens\n(O)dds\n(S)quares\n(Q)uit")
menu_choice = input().upper()
while menu_choice != 'Q':
    if menu_choice == 'E':
        for i in range(num_1, num_2):
            if i % 2 == 0:
                print(i)
    elif menu_choice == 'O':
        for i in range(num_1, num_2):
            if i % 2 == 1:
                print(i)
    else:
        for i in range(num_1, num_2):
            print(i*i)
    print("(E)vens\n(O)dds\n(S)quares\n(Q)uit")
    menu_choice = input().upper()