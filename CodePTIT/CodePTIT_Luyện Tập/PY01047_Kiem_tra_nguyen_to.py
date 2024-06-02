from math import sqrt


def isPrime (n):
    for i in range (2, (int)(sqrt(n) + 1)):
        if not n%i:
            return False
    return n > 1

for t in range (int(input())):
    n = input()
    print("YES" if isPrime(int(n[len(n)-4:])) else "NO")