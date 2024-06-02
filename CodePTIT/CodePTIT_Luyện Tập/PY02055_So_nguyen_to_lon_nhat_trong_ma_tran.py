import math

def isPrime(n):
    for i in range(3, (int)(math.sqrt(n))+1, 2):
        if not n % i:
            return False
    return n == 2 or (n > 2 and n % 2)

n, m = [int(i) for i in input().split()]
a, max = [], 0
for i in range(n):
    a += [[int(j) for j in input().split()]]
for i in range(n):
    for j in range(m):
        if a[i][j] > max and isPrime(a[i][j]):
            max = a[i][j]
if max == 0:    print('NOT FOUND')
else:
    print(max)
    for i in range(n):
        for j in range(m):
            if a[i][j] == max:
                print(f'Vi tri [{i}][{j}]')