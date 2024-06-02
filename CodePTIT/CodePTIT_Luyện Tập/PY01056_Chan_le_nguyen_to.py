from math import sqrt


def isPrime(n):
    for i in range(2, int(sqrt(n)+1)):
        if not n%i:
            return False
    return n >= 2

def isValid(n):
    for i in range(len(n)):
        if (i + int(n[i])) % 2:
            return False
    return isPrime(sum(int(i) for i in n))

for t in range(int(input())):
    print("YES" if isValid(input()) else "NO")