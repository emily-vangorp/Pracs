name = input("Enter name: ")
print("(H)ello\n(G)oodbye\n(Q)uit")
print()
menu_choice = input(">>> ").upper()
while menu_choice != 'Q':
    if menu_choice == 'H':
        print("Hello", name)
    elif menu_choice == 'G':
        print("Goodbye", name)
    else:
        print("Invalid choice")
    print("(H)ello\n(G)oodbye\n(Q)uit")
    menu_choice = input(">>> ").upper()
print("Finished.")