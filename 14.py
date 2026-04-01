def max_no(numbers):
    if not numbers:
        return None

    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest  = num
    
    return largest

print(max_no([1,2,3,4,7,8,4]))