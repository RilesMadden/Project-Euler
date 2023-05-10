# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

from math import floor
# a = 100, 101, 102... b = 100, 101, 102 ...
# multiply a1 by b1
# check if the product is a palindrome
#   if yes, assign it to the max palindrome element
#   if no, increase b1 by 1 and repeat
# repeat process until a = 999 and b = 999
# if we run into another palindrome, check if it's bigger than the max palindrome, if so, assign it.

# to check if palindrome
# convert int into a string
# split it up and put it into a list
# palindrome if n[0] = n[-1], n[1] = n[-2], n[2] = n[-3], n[3] = n[-4]
#
# palindrome = True
# j = -1
# for i in range(0, floor(n/2)):
#   if a[i] == a[j]:
#       j -= 1
#   else:
#       palindrome = False


max_palindrome = 0
a = 100
while a < 1000:
    for b in range(100, 1000):
        product_list = []
        product = a * b
        product_string = str(product)
        for number in product_string:
            product_list.append(number)
        is_palindrome = True
        j = -1
        for i in range(0, floor(len(product_list)/2)):
            if product_list[i] == product_list[j]:
                j -= 1
            else:
                is_palindrome = False
                break
        if is_palindrome == True:
            if product > max_palindrome:
                max_palindrome = product
    a += 1
print(max_palindrome)
        
# Answer = 906609
