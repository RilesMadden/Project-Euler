# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a^2 + b^2 = c^2
# For example, 3,4,5, 3^2 + 4^2 = 5^2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc

# have 3 variables, a, b, c, all of which are going to be in the form n^2 = a
# a < b < c < 1000
# 3 loops, c will increase, then b, then a
# if no a and b exist such that a2 + b2 = c2, increase c until c = 998

triplet = []
for a in range(1, 1000):
    print(f"a = {a}")
    for b in range(a+1, 1000):
        a_plus_b = a**2 + b**2
        if a_plus_b < 1000:
            upper_bound = a_plus_b
        else:
            upper_bound = 1000
        for c in range(b+1, upper_bound):
            if a < b < c:
                if a_plus_b == c**2:
                    if a + b + c == 1000:
                        triplet.append((a,b,c))

print(triplet)







