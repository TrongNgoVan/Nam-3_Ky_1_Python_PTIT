from math import sqrt

def isPrime(n):
    if n < 2:   return False
    elif n == 2:    return True
    elif n%2 == 0:  return False
    else:
        for k in range(3, int(sqrt(n)) + 1, 2):
            if n%k == 0:    return False
    return True

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])
for i in range(n):
    for j in range(m):
        print ("1 " if isPrime(a[i][j]) else "0 ", end='')
    print()