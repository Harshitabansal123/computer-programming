#15. Extract All Numbers from a String
#Problem: Extract all numbers from the string "abc123def456ghi789".

import re
s = "abc123def456ghi789"
numbers = re.findall(r'\d+', s)
print(numbers)
