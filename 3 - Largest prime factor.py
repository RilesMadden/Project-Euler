# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from is_prime_function import is_prime
from math import floor, sqrt

n = 600851475143
# My long solution
def find_largest_prime_factor(n):
    prime_factors = []
    for i in range(1, floor(n/2), 2):
        if is_prime(i) == True:
            if n % i == 0:
                prime_factors.append(i)
    if len(prime_factors) == 0:
        print(f'{n} is a prime number')
    
    else:
        max_prime_factor = max(prime_factors)
        print(max_prime_factor)

find_largest_prime_factor(n)

# Better solution

# if n % 2 == 0:
#     lastFactor = 2
#     n = n / 2
#     while n % 2 == 0:
#         n = n / 2
# else:
#     lastFactor = 1
# factor = 3
# maxFactor = sqrt(n)
# while n > 1 and factor <=maxFactor:
#     if n % factor == 0:
#         n = n / factor
#         lastFactor = factor
#         while n % factor == 0:
#             n = n / factor
#         maxFactor = sqrt(n)
#     factor += 2
# if n == 1:
#     print(lastFactor)
# else:
#     print(n)



