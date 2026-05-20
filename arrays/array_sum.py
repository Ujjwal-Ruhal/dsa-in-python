def array_sum(numbers):
    if not numbers:
        return None

    total = 0

    for num in numbers:
        total += num

    return total


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = array_sum(numbers)

if result is None:
    print("List is empty")
else:
    print("Sum of array is:", result)