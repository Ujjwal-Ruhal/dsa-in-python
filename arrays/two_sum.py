def two_sum(numbers, target):
    """
    Find the indices of two numbers whose sum is equal to target.

    Example:
    numbers = [3, 2, 4]
    target = 6

    Return:
    (1, 2)
    """

    # Handle empty input
    if not numbers:
        return None

    # Dictionary to store:
    # number -> index
    seen = {}

    # Traverse the array with both index and value
    for i, num in enumerate(numbers):

        # Calculate the number needed to reach the target
        needed = target - num

        # Check if the needed number was seen before
        if needed in seen:

            # Return:
            # index of needed number
            # current index
            return (seen[needed], i)

        # Store current number and its index
        # so future elements can use it
        # Store only first occurrence
        if num not in seen:
            seen[num] = i

    # No valid pair found
    return -1


# Take array input from user
numbers = list(map(int,input("Enter numbers separated by spaces: ").split()))
# Take target input
target = int(input("Enter target: "))
result = two_sum(numbers, target)

# Handle different cases
if result is None:
    print("Array is empty")

elif result == -1:
    print("No pair found")

else:
    print("Target found at indices:", result)