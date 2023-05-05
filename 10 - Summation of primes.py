# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
from is_prime_function import is_prime
import time
import math

# simple solution, check every number between 1 and 2,000,000
# if the number is prime, add to total
# if not, don't do anything

# further optimizations would include not checking even numbers, using math rule that primes greater than 9 can only be written as 6*k +- 1

# first account the edge cases which are numbers 2-9, 2,3,5,7
# maybe use a while loop to make sure that 6k +- 1 stays less than 2million

time_1 = time.time()
total_sum = 2
for i in range(1,2000000,2):
    if is_prime(i) == True:
        total_sum += i
time_2 = time.time()
print(total_sum)
print(time_2 - time_1)

# time_1 = time.time()
# total_sum = 17
# counter = 2
# counter_times_six = 6*counter
# counter_times_six_minus_1 = 6*counter - 1
# counter_times_six_plus_1 = 6*counter + 1
# while counter_times_six_minus_1 < 20000000 or counter_times_six_plus_1 < 20000000:
#     a = counter_times_six_minus_1
#     b = counter_times_six_plus_1
#     if is_prime(a) == True:
#         total_sum += a
#     if is_prime(b) == True:
#         total_sum += b
#     counter += 1
# time_2 = time.time()

# print(total_sum)
# print(time_2 - time_1)


# target = 2000000
# time_1 = time.time()
# total_sum = 17
# counter = 2
# for i in range(1,math.floor((target-1)/6)+1):
#     counter_times_six_minus_1 = 6*counter - 1
#     counter_times_six_plus_1 = 6*counter + 1
#     if is_prime(counter_times_six_minus_1) == True:
#         total_sum += counter_times_six_minus_1
#     if is_prime(counter_times_six_plus_1) == True:
#         total_sum += counter_times_six_plus_1
#     counter += 1
# time_2 = time.time()

# print(total_sum)
# print(time_2 - time_1)