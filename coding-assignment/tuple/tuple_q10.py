#Problem: Convert a List of Tuples into a Tuple of Lists
def list_of_tuples_to_tuple_of_lists(lst):
    return tuple([list(t) for t in lst])

# Test case
lst = [(1, 2, 3), (4, 5), (6, 7, 8)]
print(list_of_tuples_to_tuple_of_lists(lst))  # Output: ([1, 2, 3], [4, 5], [6, 7, 8])
