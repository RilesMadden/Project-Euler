from is_prime_function import is_prime

# every prime greater than 9 can be written as 6k +- 1

prime_counter = 4 # this takes care of 2,3,5,7
latest_prime = 0
k = 2
while prime_counter < 10001:
    a = 6*k - 1
    b = 6*k + 1
    if is_prime(a):
        prime_counter += 1
        latest_prime = a
    if is_prime(b):
        prime_counter += 1
        latest_prime = b
    k += 1
print(prime_counter)
print(latest_prime)



