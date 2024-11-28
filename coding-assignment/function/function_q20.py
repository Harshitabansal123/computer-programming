#20. Find the Intersection of Two Lists
#Problem: Write a function that takes two lists and returns a list of elements that are common in both lists (intersection).

def intersection_of_lists(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(intersection_of_lists(list1, list2))
