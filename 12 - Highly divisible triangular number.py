# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 
# The first ten terms would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?

# need to keep track of an increasing sum
# need to keep track of a natural number counter to add to increasing num
# loop and check each increasing sum for divisors and add to list
# once the list reaches 500, stop
# the increasing sum is our answer

import math

triangle_sum = 1
counter = 2
list_of_divisors = []
while len(list_of_divisors) < 500:
    list_of_divisors.clear()
    triangle_sum += counter
    for i in range(1, math.floor(triangle_sum/2)+1):
        if triangle_sum % i == 0:
            list_of_divisors.append(i)
    counter += 1

print(triangle_sum)

# Answer = 76576500





