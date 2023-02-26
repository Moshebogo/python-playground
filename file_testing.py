import sys

def  show():
    with open("database.txt") as file:
        counter = 1
        for line in file:
            print(f'Car-{counter}: {line}', end='')
            counter += 1               

def cars():
    car = (input("Which car would you like to add to the file? "))
    with open("database.txt", "a") as file:
        file.write(car + "\n")


if __name__ == '__main__':
    if sys.argv[1].lower() == '--list':
        show()
    else:
        cars()    