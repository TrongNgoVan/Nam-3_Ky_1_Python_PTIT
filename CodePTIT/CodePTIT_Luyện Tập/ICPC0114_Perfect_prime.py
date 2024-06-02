from math import sqrt

maxVal = int(1e7 + 5)
def isPrime (n):
    for i in range(2, int(sqrt(n) + 1)):
        if not n%i:
            return False
    return n >= 2
def checkDigits (n):
    for i in n:
        if not isPrime(int(i)):
            return False
    return True

for t in range(int(input())):
    n = input()
    print("Yes" if isPrime(int(n)) and isPrime(int(n[::-1])) and isPrime(sum(int(i) for i in n)) and checkDigits(n)  else "No")
