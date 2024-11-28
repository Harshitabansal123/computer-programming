#Find GCD(greatest common divisor) of Two Numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(56, 98))  # Output: 14
