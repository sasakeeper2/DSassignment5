# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    for num in numbers:
        if numbers.count(num) == max(numbers.count(n) for n in numbers):
            return num
        else:
            continue

"""
Time and Space Analysis for problem 1:
- Best-case: O(n)
- Worst-case: O(n^2)
- Average-case: O(n^2)
- Space complexity: O(1)
- Why this approach? Simple and straightforward using built-in methods.
- Could it be optimized? Yes, using a dictionary to count the times the number show up would reduce time complexity to O(n).
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

"""
Time and Space Analysis for problem 2:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? Efficiently tracks seen elements using a set while preserving order with a list.
- Could it be optimized? This is already the best option for the problem.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    pairs = []
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((min(num, complement), max(num, complement)))
        seen.add(num)
    return list(set(pairs))

"""
Time and Space Analysis for problem 3:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? Uses a set for O(1) lookups to find complements efficiently.
- Could it be optimized? This is already the best option for the problem rules.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 4
    lst = [None] * capacity
    size = 0

    for i in range(n):
        if size == capacity:
            print(f"Resizing from {capacity} to {capacity * 2}")
            new_lst = [None] * (capacity * 2)
            for j in range(size):
                new_lst[j] = lst[j]
            lst = new_lst
            capacity *= 2
        lst[size] = i
        size += 1
    return lst[:size]

"""
Time and Space Analysis for problem 4:
- When do resizes happen? When the current size equals capacity.
- What is the worst-case for a single append? O(n) during a resize.
- What is the amortized time per append overall? O(1)
- Space complexity: O(n)
- Why does doubling reduce the cost overall? Because it reduces the frequency of resizing operations.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums

"""
Time and Space Analysis for problem 5:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(1)
- Why this approach? In-place modification saves space.
- Could it be optimized? This is already the best oprion for both time and space.
"""
print(most_frequent([1, 3, 2, 3, 4, 1, 3]))  # Example usage
print(remove_duplicates([4, 5, 4, 6, 5, 7]))  # Example usage
print(find_pairs([1, 2, 3, 4], 5))  # Example usage
print(add_n_items(6))  # Example usage
print(running_total([1, 2, 3, 4]))  # Example usage