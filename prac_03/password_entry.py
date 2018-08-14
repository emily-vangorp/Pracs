"""Emily Van Gorp"""

MIN_LENGTH = 6

def main():
    password = get_password()
    print_stars(password)


def print_stars(password):
    for char in password:
        print('*', end='')


def get_password():
    password = input("Password: ")
    while len(password) < MIN_LENGTH:
        print("Too short.")
        password = input("Password: ")
    return password


main()
