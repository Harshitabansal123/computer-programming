# Define a function 'test' that takes a dictionary 'dictt' as an argument.Use a expression to calculate the sum of lengths of all values in the input dictionary.
def test(dictt):
    result = sum((len(values) for values in dictt.values()))
    return result

color = {'#FF0000':'Red', '#800000':'Maroon', '#FFFF00':'Yellow', '#808000':'Olive'}

print("Original dictionary:")
print(color)
print("Total length of all values of the said dictionary with string values:")
print(test(color)) 
