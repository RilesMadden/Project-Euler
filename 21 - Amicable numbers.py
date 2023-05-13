# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

import math
from is_prime_function import is_prime

def amicable_sum(num):
    num_sum = 0
    for n in range(1, num):
        if num % n == 0:
            num_sum += n
    return num_sum

# mine
# target = 1000
# amicable_sums = 0
# amicable_list = []
# for i in range(1,target):
#     if is_prime(i) == False:
#         i_sum = amicable_sum(i)
#         for j in range(1,target):
#             if is_prime(j) == False:
#                 if i != j:
#                     j_sum = amicable_sum(j)
#                     if i_sum == j_sum and i not in amicable_list and j not in amicable_list:
#                         amicable_sums += i
#                         amicable_sums += j
#                         amicable_list.append(i)
#                         amicable_list.append(j)

# print(amicable_list)
# print(amicable_sums)

# print(amicable_sum(220))
# print(amicable_sum(284))

# Project Euler solution
# sum = 0
# for a in range(2, 10000):
#     b = amicable_sum(a)
#     if b > a:
#         if amicable_sum(b) == a:
#             sum += a
#             sum += b
# print(sum)
