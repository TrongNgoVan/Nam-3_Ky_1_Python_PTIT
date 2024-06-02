import math

def isReversible(n):
    return len(n) >= 2 and n == n[::-1]

n, m = [int(i) for i in input().split()]
a, max = [], 0
for i in range(n):
    a += [[j for j in input().split()]]
for i in range(n):
    for j in range(m):
        if int(a[i][j]) > max and isReversible(a[i][j]):
            max = int(a[i][j])
if max == 0:    print('NOT FOUND')
else:
    print(max)
    for i in range(n):
        for j in range(m):
            if int(a[i][j]) == max:
                print(f'Vi tri [{i}][{j}]')