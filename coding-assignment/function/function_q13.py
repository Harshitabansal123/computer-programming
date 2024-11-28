#13. Find All Divisors of a Number
#Write a function that returns all divisors of a given number.

def find_divisors(n):
    divisors = [i for i in range(1, n+1) if n % i == 0]
    return divisors
print(find_divisors(28))
