from math import gcd


l, r = [int(i) for i in input().split()]
for i in range (l, r+1):
    for j in range (i+1, r+1):
        if gcd(i, j) == 1:
            for k in range (j+1, r+1):
                if gcd(j, k) == 1 and gcd(i, k) == 1:
                    print("({}, {}, {})".format(i, j, k))