# Define a function 'test' that clears the list values within a dictionary.
def test(dictionary):
    for key in dictionary:
        dictionary[key].clear()
    return dictionary

dictionary = { 
    'C1': [10, 20, 30], 
    'C2': [20, 30, 40],
    'C3': [12, 34]
}
print("Original Dictionary:")
print(dictionary)

print("Clear the list values in the said dictionary:")
print(test(dictionary)) 
