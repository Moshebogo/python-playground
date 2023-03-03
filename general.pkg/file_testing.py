import sys

def  show():
    with open("database.txt") as file:
        for i, line in enumerate(file):
            print(f'Car # {i+1}: {line}', end='')

def cars():
    car = (input("Which car would you like to add to the file? "))
    with open("database.txt", "a") as file:
        file.write(car + "\n")

my_file = open("database.txt")
# for line in my_file:
#     print(line.rstrip())
my_file.close()
print(my_file)
# show()
# if __name__ == '__main__':
#     if sys.argv[1].lower() == '--list':
#         show()
#     else:
#         cars()    