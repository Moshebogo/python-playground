def find_odd_nums_1(numbers):
    return [num for num in numbers if num % 2 != 0]

def find_odd_nums_2(nums):
    odd_nums = []
    for num in nums:
        if num % 2 != 0:
            odd_nums.append(num)
    return odd_nums      

def find_odd_nums_3(nums):
    for num in nums: 
        if num % 2 != 0:
            yield num

def find_odd_nums_4(nums):
    odd_nums = []
    for num in nums:
        odd_nums.append(num) if num % 2 != 0 else None
    return odd_nums    
                    
    


print("expecting => [1, 3, 5, 7, 9]")
print(find_odd_nums_1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print()

print("expecting => [1, 3, 5, 7, 9]")
print(find_odd_nums_2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print()

print("expecting => [1, 3, 5, 7, 9]")
print(list(find_odd_nums_3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

print()

print("expecting => [1, 3, 5, 7, 9]")
print((find_odd_nums_4([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))