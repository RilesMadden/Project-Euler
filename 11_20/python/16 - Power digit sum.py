# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

num = 2**1000
num_string = str(num)
num_list = []
for digit in num_string:
    num_list.append(digit)

sum_of_digits = 0
for digit in num_list:
    sum_of_digits += int(digit)
print(sum_of_digits)

# Answer = 1366