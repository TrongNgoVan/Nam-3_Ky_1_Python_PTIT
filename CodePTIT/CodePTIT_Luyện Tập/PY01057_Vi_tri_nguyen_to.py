from math import sqrt


prime = [True for i in range(505)]
prime[0] = prime[1] = False

for i in range(2, int(sqrt(505) + 1)):
    if prime[i]:
        for j in range(i*2, 505, i):
            prime[j] = False

def isValid (n):
    for i in range(len(n)):
        if prime[i] + prime[int(n[i])] == 1:
            return False
    return True

for t in range(int(input())):
    print("YES" if isValid(input()) else "NO")
