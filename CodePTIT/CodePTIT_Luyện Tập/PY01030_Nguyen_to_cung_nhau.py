from math import gcd


n, k = [int(i) for i in input().split()]
cou = 0
for i in range (10**(k-1), 10**k - 1):
    if gcd(i, n) == 1:
        cou += 1
        print(i, end=' ')
    if cou == 10:
        print()
        cou = 0