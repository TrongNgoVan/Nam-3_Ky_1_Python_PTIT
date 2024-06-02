import math

def isPrime(n):
    for i in range(3, (int)(math.sqrt(n))+1, 2):
        if not n % i:
            return False
    return n == 2 or (n > 2 and n % 2)
def findIndex(b):
    l, r = 0, sum(b, 0)
    for i in range(len(b)):
        l += b[i]
        r -= b[i]
        if isPrime(l) and isPrime(r):
            print(i)
            return
    print('NOT FOUND')

n = int(input())
b = list(dict.fromkeys([int(i) for i in input().split()]))
findIndex(b)