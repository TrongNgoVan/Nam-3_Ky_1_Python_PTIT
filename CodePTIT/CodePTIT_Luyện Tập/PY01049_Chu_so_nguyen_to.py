from math import sqrt


isPrime = [1]*505
def sievePrime ():
    isPrime[0] = isPrime[1] = 0
    for i in range(2, (int)(sqrt(500) + 1)):
        if isPrime[i]:
            for j in range (i*2, 500, i):
                isPrime[j] = 0
sievePrime()

def isValid (n):
    prime = nonprime = 0
    for i in n:
        if isPrime[int(ord(i) - ord('0'))]:
            prime += 1
        else:
            nonprime += 1
    return prime > nonprime and isPrime[len(n)]

for t in range(int(input())):
    n = input()
    print("YES" if isValid(n) else "NO")