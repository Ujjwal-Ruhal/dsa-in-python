def palindrome_check(word):
    if not word:
        return None

    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return False

        left += 1
        right -= 1

    return True


word = input("Enter a word: ")

result = palindrome_check(word)

if result is None:
    print("Input is empty")
else:
    print(result)