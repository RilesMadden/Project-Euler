import math

def is_prime(n):
    n = abs(n)
    # 0 and 1 are not prime
    if n == 0 or n == 1:
        return False
    # 2 and 3 are prime
    elif n < 4:
        return True
    # all even numbers except 2 are not prime
    elif n % 2 == 0:
        return False
    # we have excluded 4, 6, 8
    elif n < 9:
        return True
    # check if 9 or divisible by 3 for future numbers
    elif n % 3 == 0:
        return False
    else:
        r = math.floor(math.sqrt(n)) # find the next closest integer to the square root of n
        f = 5
        while f <= r:
            if n % f == 0:
                return False
                break
            elif n % (f + 2) == 0:
                return False
                break
            else:
                f += 6
        return True



# target number n
# check every number between 1 and n-1
# if any n % number == 0, then it's not prime
# if no n % number == 0, then it is prime
# optimizations: there won't be any number bigger than n/2 that's a factor, so only go from 1 to n/2
# you can skip by 2 after the number 2, cause any even isnt prime

# def check_is_prime(n):
#     is_prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             is_prime = False
#     return is_prime

# print(check_is_prime(19))


