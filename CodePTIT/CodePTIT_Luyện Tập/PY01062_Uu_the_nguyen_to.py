from math import sqrt


p = [1 for i in range(int(1e5))]
p[0] = p[1] = 0
for i in range(2, int(sqrt(1e5)) + 1):
    if p[i]:
        for j in range(i*2, int(1e5), i):
            p[j] = 0

def isValid (n):
    prime = 0
    for i in n:
        if p[int(i)]:
            prime += 1
    return prime > len(n) - prime and p[len(n)]

for t in range(int(input())):
    print("YES" if isValid(input()) else "NO")