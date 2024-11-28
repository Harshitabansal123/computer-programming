#14. Find Missing Number in a List
#Given a list of integers from 1 to n with one number missing, write a function to find the missing number.

def find_missing_number(lst, n):
    total = n * (n + 1) // 2
    return total - sum(lst)
print(find_missing_number([1, 2, 4, 5, 6], 6))
