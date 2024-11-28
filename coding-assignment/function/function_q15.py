#15. Find Unique Elements in a List
#Write a function that returns a list of unique elements from the given list.

def unique_elements(lst):
    return list(set(lst))
print(unique_elements([1, 2, 3, 2, 1]))
