from math import gcd, sqrt


def isPrime (n):
    for i in range (2, int(sqrt(n)) + 1):
        if not n%i:
            return False
    return n >= 2

for t in range(int(input())):
    a, b = [int(i) for i in input().split()]
    print("YES" if isPrime(sum(int(i) for i in str(gcd(a, b)))) else "NO")