from math import gcd, sqrt


def isPrime(n):
    if n < 2:
        return False
    square = int(sqrt(n) +1)
    for i in range(2, square):
        if not n%i:
            return False
    return True

for i in range(int(input())):
    n = int(input())
    cou = 0
    for j in range(1, n):
        if gcd(j, n) == 1:
            cou += 1
    print("YES" if isPrime(cou) else "NO")