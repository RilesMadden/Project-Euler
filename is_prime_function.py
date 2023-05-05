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
