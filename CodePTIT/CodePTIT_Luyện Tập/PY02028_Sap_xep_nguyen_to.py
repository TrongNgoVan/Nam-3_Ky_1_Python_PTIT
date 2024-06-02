import math

def isPrime(n):
    for i in range(3, (int)(math.sqrt(n))+1, 2):
        if not n % i:
            return False
    return n == 2 or (n > 2 and n % 2)

n, list = int(input()), [int(i) for i in input().split()]
prime = sorted([i for i in list if isPrime(i)])
index = 0
for i in list:
    if not i in prime:  print(i, end=' ')
    else:
        print(prime[index], end=' ')
        index += 1