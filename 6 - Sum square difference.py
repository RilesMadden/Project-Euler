# The sum of the squares of the first ten natural numbers is 1^2 + 2^2 + ... 10^2 = 385
# The square of the sum of the first ten natural numbers is (1 + 2 .... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Find the sum of the squares between 1 and 100
sum_of_squares = 0
for i in range(1,101):
    sum_of_squares += i**2

# Find the square of the sums between 1 and 100
square_of_sums = 0
for i in range(1,101):
    square_of_sums += i
square_of_sums = square_of_sums ** 2

# Find the difference
print(square_of_sums - sum_of_squares)