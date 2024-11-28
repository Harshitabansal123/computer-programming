# Check If a Number is Armstrong
def is_armstrong(n):
    num_digits = len(str(n))
    return n == sum(int(digit) ** num_digits for digit in str(n))

print(is_armstrong(153))  # Output: True
print(is_armstrong(123))  # Output: False
