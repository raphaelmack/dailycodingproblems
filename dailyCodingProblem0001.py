"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""

def check_if_sum(array, k):
    potential_numbers = set()
    for i in array:
        if i in potential_numbers:
            return True
        potential_numbers.add(k - i)
    return False


array = [10, 15, 3, 7]
k = 17
assert check_if_sum(array, k)