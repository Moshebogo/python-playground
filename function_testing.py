# Lists of numbers and letters for testing functions
numbers = [1, 2, 3, 4 , 5, 6, 7, 8, 9, 10]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# returns numbers that are lower then 300
def lower_than_300(arg):
     return arg < 300

# square all numbers in list
def square(arg):
    return arg * arg

# combines 2 iterables
def combine():
   return list(zip(numbers, letters))

# returns true/false list
def true_and_false(numbers, letters):
    zipped = list(zip(numbers, letters))
    finished = [(num % 2 == 0, num, letter) for num, letter in zipped]
    for item in finished:
        print(item)

# prints everything
def printer():
    print('This function executes all functions.')   
    # print('All numbers squared:')
    # print(list(map(square, numbers)))
    # print()
    # print('All numbers < 300:')
    # print(list(filter(lower_than_300, numbers)))
    # print()
    # print(f"""Combines all item in "numbers" and "letters" :
    # {combine()}. List Length: {len(combine())}.""")
    # print()
    # true_and_false(numbers, letters)
    # print()
    # true_and_false(numbers, letters)
# printer()

# lambda functions
print((lambda x: x + x)(5))