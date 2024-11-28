#19. Sum of Square of Numbers in a List
#Write a function that returns the sum of the square of all numbers in a list.

def sum_of_squares(lst):
    return sum(x**2 for x in lst)
print(sum_of_squares([1, 2, 3, 4]))
