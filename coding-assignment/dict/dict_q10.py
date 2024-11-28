# Define a function 'value_check' that checks if all values in a dictionary are equal to a given value 'n'.
def value_check(students, n):
    result = all(x == n for x in students.values())
    return result

students = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}

print("Original Dictionary:")
print(students)
n = int(input("Enter Number: "))
print("Check all are", n, "in the dictionary.")
print(value_check(students, n)) 
