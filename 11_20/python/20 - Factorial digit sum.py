# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

start = 100
factorial_product = start

while start > 1:
    factorial_product *= (start-1)
    start -= 1

list_of_digits = []
factorial_product_string = str(factorial_product)
for num in factorial_product_string:
    list_of_digits.append(int(num))

sum = sum(list_of_digits)
print(sum)

# Answer = 648