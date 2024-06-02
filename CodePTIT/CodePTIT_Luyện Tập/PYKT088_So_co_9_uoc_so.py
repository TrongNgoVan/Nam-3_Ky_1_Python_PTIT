from math import sqrt

res, n = 0, int(input())
m = int(sqrt(n)) + 1

p = [i for i in range(m)] #p[i] là ước nt của i
for i in range(2, int(sqrt(m))):
    if p[i] == i:
        for j in range(i*i, m, i):
            if p[j] == j: p[j] = i

for i in range(2,m):
    i1 = p[i]
    i2 = i // i1
    if i2 == p[i//i1] and i1 != i2 and i2 != 1:  # kiểm tra i là tích của 2 snt
        res += 1
    elif p[i] == i and pow(i, 8) <= n:  
        res += 1        

print(res)
