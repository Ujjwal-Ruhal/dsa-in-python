# DSA Notes

## Problem Solving Process

For every problem:

1. Understand the problem
2. Solve manually on paper
3. Write the algorithm
4. Analyze time complexity
5. Write code
6. Dry run the code
7. Optimize if possible

---

# Time Complexity Cheat Sheet

| Pattern         | Complexity   |
| --------------- | ------------ |
| Direct access   | O(1)         |
| Single loop     | O(n)         |
| Nested loops    | O(n²)        |
| Binary Search   | O(log n)     |
| Sorting         | O(n log n)   |
| Hash Map Lookup | O(1) average |

---

# Arrays

## Find Maximum Element

Pattern:
Traversal

Approach:

- Assume first element is maximum
- Traverse array
- Update max when larger element is found

Time Complexity: O(n)

Space Complexity: O(1)

---

## Find Minimum Element

Pattern:
Traversal

Approach:

- Assume first element is minimum
- Traverse array
- Update minimum when smaller element is found

Time Complexity: O(n)

Space Complexity: O(1)

---

## Array Sum

Pattern:
Running Total

Approach:

- Initialize total = 0
- Add each element to total

Time Complexity: O(n)

Space Complexity: O(1)

---

## Count Even Numbers

Pattern:
Counting

Approach:

- Initialize count = 0
- If num % 2 == 0
- Increment count

Time Complexity: O(n)

Space Complexity: O(1)

---

## Linear Search

Pattern:
Searching

Approach:

- Traverse array
- Compare current element with target
- Return index if found
- Return -1 if not found

Time Complexity: O(n)

Space Complexity: O(1)

Learning:

- enumerate() gives both index and value

---

# Two Pointers Pattern

Definition:

Use two indices that move toward each other.

Example:

left = 0
right = len(arr) - 1

while left < right:

# work

left += 1
right -= 1

---

## Reverse Array

Pattern:
Two Pointers

Approach:

- First pointer at start
- Second pointer at end
- Swap values
- Move pointers inward

Time Complexity: O(n)

Space Complexity: O(1)

---

## Palindrome Check

Pattern:
Two Pointers

Approach:

- Compare first and last character
- If mismatch → False
- Continue until pointers meet
- If all match → True

Time Complexity: O(n)

Space Complexity: O(1)

Important:
Do not reverse the entire string.
Compare directly.

---

# Hash Map Pattern

Definition:

Store data as:

value -> index

Example:

{
5: 0,
8: 1
}

Benefits:

- Fast lookup
- Average O(1) search

---

## Two Sum

Pattern:
Hash Map

Approach:

needed = target - current_number

If needed exists in seen:
return indices

Else:
store current number

Pseudo Logic:

seen = {}

for each number:
needed = target - current_number

```
if needed in seen:
    return answer

store current number
```

Time Complexity: O(n)

Space Complexity: O(n)

Mistakes I Made:

- Used while True
- Used numbers.index()
- Searched entire list repeatedly
- Returned dictionary instead of indices

Lessons:

- Use enumerate()
- Use Hash Map lookup
- Avoid unnecessary searches

---

# Python Concepts Learned

## enumerate()

Purpose:

Get index and value together.

Example:

for i, num in enumerate(numbers):
pass

Returns:

(0, value)
(1, value)
(2, value)

---

## Dictionary

Store:

key -> value

Example:

seen = {
5: 0,
8: 1
}

Lookup:

if 5 in seen

Complexity:

O(1) average

---

# Important Interview Rules

1. First solve manually
2. Write brute force approach
3. Identify bottleneck
4. Optimize
5. Explain complexity

---

# Current Patterns Mastered

✓ Traversal

✓ Running Total

✓ Counting

✓ Searching

✓ Two Pointers

✓ Hash Map Basics

---

# Next Topics

- Contains Duplicate
- Hash Set
- Prefix Sum
- Sliding Window
- Binary Search
- Recursion
- Linked List
- Stack
- Queue
- Trees
- Graphs
- Dynamic Programming



# Contains Duplicate

Pattern:
Hash Set

Approach:
1. Create an empty set.
2. Traverse the array.
3. If current number already exists in set:
   return True
4. Otherwise add it to set.
5. If loop completes:
   return False

Time Complexity: O(n)

Space Complexity: O(n)

Learning:
- Set lookup is O(1) average.
- Set insert is O(1) average.
- Better than using a list.


# Valid Anagram

Pattern:
Frequency Counting
Hash Map

Approach:
1. Count frequency of characters in first word.
2. Count frequency of characters in second word.
3. Compare both dictionaries.

Time Complexity: O(n)

Space Complexity: O(n)

Learning:
Dictionary can be used for frequency counting.
Two dictionaries are equal if all keys and values match.