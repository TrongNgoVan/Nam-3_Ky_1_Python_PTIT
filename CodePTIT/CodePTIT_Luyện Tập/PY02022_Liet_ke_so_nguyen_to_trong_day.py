from math import sqrt


def isPrime (n):
    for i in range(2, int(sqrt(n)+1)):
        if not n%i: return False
    return n >= 2

n = int(input())
a = [int(i) for i in input().split()]
for i in list(dict.fromkeys(a)):
    if isPrime(i):
        print(i, a.count(i))