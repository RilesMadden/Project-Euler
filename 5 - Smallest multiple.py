# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# start counter at 20
# set a variable is_divis_by_all = False
# check if 20 is divisible by 2
# if yes, check if divisible by 3
# if no, break and add one to counter
# if divisible by 3, check if by 4, etc
# as soon as the repeat gets to 20, trip is_divis_by_all to True
# counter is the answer

smallest_positive_number = 20
is_divisible_by_all = False


while is_divisible_by_all == False:
    tripped = False
    for i in range(11,21):
        if smallest_positive_number % i != 0:
            tripped = True
            break
    if tripped == True:
        smallest_positive_number += 20
    else:
        is_divisible_by_all = True    
    
print(smallest_positive_number)
