def contains_duplicate(numbers):
    if not numbers:
        return None
    
    seen = set()
    for num in numbers:
        if num in seen:
            return True
        seen.add(num)
    return False
    
numbers = list(map(int,input("Enter numbers separated by spaces: ").split()))
result = contains_duplicate(numbers)

if result is None:
    print("Array is empty")

else:
    print(result)