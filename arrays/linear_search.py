def linear_search(numbers, target):
    if not numbers:
        return None

    for i, num in enumerate(numbers):
        if num == target:
            return i

    return -1


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter your target: "))

result = linear_search(numbers, target)

if result is None:
    print("List is empty")
elif result == -1:
    print("Target not found")
else:
    print("Target found at index:", result)