#Problem: Find the Second Largest Element in a Tuple
def second_largest(tpl):
    unique_tpl = sorted(set(tpl), reverse=True)
    return unique_tpl[1] if len(unique_tpl) > 1 else None

# Test case
tpl = (10, 20, 30, 40, 20, 10)
print(second_largest(tpl))  # Output: 30
