from math import gcd


n = int(input())
a = sorted([int(i) for i in input().split()])

for i in range(n-1):
    for j in range(i+1, n):
        if gcd(a[i], a[j]) == 1:
            print(a[i], a[j], sep=' ')