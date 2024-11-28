#Problem: Flatten a Tuple of Tuples
def flatten_tuple(tpl):
    return tuple(item for subtuple in tpl for item in subtuple)

# Test case
tpl = ((1, 2), (3, 4), (5, 6))
print(flatten_tuple(tpl))  # Output: (1, 2, 3, 4, 5, 6)
