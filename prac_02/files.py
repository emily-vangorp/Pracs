NAMES_FILE = "names.txt"
numbers_added = 0
out_file = open(NAMES_FILE, 'w')
name = input("Enter your name: ")
print(name, file=out_file)
out_file = open(NAMES_FILE, 'r')
name = out_file.read()
print("Your name is {}".format(name))
out_file.close()
out_file = open("numbers.txt", 'r')
for line in out_file:
    numbers_added = numbers_added + int(line)
print(numbers_added)
