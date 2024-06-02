from math import sqrt


maxVal = int(1e6+5)
p = [1] * maxVal
p[0] = p[1] = 0
for i in range(2, int(sqrt(maxVal))):
    if p[i]:
        for j in range(i*2, maxVal, i):
            p[j] = 0

for t in range(int(input())):
    n = int(input())
    for i in range(11, n):
        j = int(str(i)[::-1])
        if i < j and j < n and p[i] and p[j]:
            print(i, j, end=' ')
    print()