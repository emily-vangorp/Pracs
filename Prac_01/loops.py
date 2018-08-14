for i in range(1, 21, 2):
    print(i, end=' ')
print()
for i in range(0, 100, 10):
    print(i, end=' ')
print()
for i in range(20, 0, -1):
    print(i, end=' ')
print()
star_no = int(input("Stars: "))
for i in range(star_no):
    print("*", end=' ')
for count in range(0, star_no + 1):
    for i in range(count):
        print("*", end=' ')
    print()
print()
