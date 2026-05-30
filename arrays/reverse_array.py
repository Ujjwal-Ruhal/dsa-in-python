def reverse_array(numbers):
    if not numbers:
        return None

    left = 0
    right = len(numbers) - 1

    while left < right:
        numbers[left], numbers[right] = numbers[right], numbers[left]

        left += 1
        right -= 1

    return numbers


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = reverse_array(numbers)

if result is None:
    print("Array is empty")
else:
    print("Reverse array is:", result)