def valid_anagram(first_word, second_word):
    # If lengths are different, they cannot be anagrams
    if len(first_word) != len(second_word):
        return False

    first_freq = {}
    second_freq = {}

    # Count frequency of characters in first word
    for char in first_word:
        if char in first_freq:
            first_freq[char] += 1
        else:
            first_freq[char] = 1

    # Count frequency of characters in second word
    for char in second_word:
        if char in second_freq:
            second_freq[char] += 1
        else:
            second_freq[char] = 1

    # Compare both frequency dictionaries
    return first_freq == second_freq


first_word = input("Enter first word: ")
second_word = input("Enter second word: ")

result = valid_anagram(first_word, second_word)

print(result)