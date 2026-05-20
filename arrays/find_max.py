def find_max(numbers):
    if not numbers:
        return None

    max_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num


numbers = list(map(int, input("Enter numbers separated by space: ").split()))
max_value = find_max(numbers)

if max_value is None:
    print("List is empty.")
else:
    print(f"Max number is: {max_value}")