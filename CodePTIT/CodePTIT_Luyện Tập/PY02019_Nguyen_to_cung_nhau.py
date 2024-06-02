from math import gcd

n = int(input())
a = sorted(list(map(int, input().strip().split())))
for i in range(n-1):
    for j in range(i+1, n):
        if (gcd(a[i], a[j]) == 1):
            print(a[i], a[j])
