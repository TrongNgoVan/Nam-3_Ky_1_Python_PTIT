from math import sqrt


MAX_VAL = int(1e6 + 5)
p = [1] * MAX_VAL
p[0] = p[1] = 0
for i in range(2, int(sqrt(MAX_VAL))):
    if p[i]:
        for j in range(i*2, MAX_VAL, i):
            p[j] = 0;

for t in range(int(input())):
    res = 0
    for i in range(int(input()) - 5):
        if p[i] and (p[i+2] or p[i+4]) and p[i+6]:  res += 1
    print(res)