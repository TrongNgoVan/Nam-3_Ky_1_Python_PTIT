from math import sqrt

def isPrime(n):
    if n < 2:   return False
    elif n == 2:    return True
    elif n%2 == 0:  return False
    else:
        for k in range(3, int(sqrt(n)) + 1, 2):
            if n%k == 0:    return False
    return True

for t in range(int(input())):
    n = input()
    print("YES" if isPrime(sum(int(i) for i in n)) else "NO")