def find_min(numbers):
    if not numbers:
        return None

    min_num = numbers[0]

    for num in numbers:
        if num < min_num:
            min_num = num

    return min_num


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = find_min(numbers)

if result is None:
    print("List is empty")
else:
    print("Min number is:", result)