def count_even(numbers):
    if not numbers:
        return None

    count = 0

    for num in numbers:
        if num % 2 == 0:
            count += 1

    return count


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = count_even(numbers)

if result is None:
    print("List is empty")
else:
    print("Total even numbers are:", result)