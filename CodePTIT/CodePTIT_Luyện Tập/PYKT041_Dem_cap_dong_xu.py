from math import comb


a, n, res = [], int(input()), 0
for i in range(n):
    a += [[i for i in input()]]
for i in range(n):
    res += comb(a[i].count('C'), 2)
for i in range(n):
    cnt = 0
    for j in range(n):
        if a[j][i] == 'C':
            cnt += 1
    res += comb(cnt, 2)
print(res)