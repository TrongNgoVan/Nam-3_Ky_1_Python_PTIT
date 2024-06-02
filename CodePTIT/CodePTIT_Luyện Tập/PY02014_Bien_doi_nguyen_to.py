p = []
a = [1] * int(1e5)
a[0] = a[1] = 0
for i in range(2, int(1e4)+1):
    if a[i] == 1:
        p += [i]
        for j in range(i*i, int(1e4)+1, i):
            a[j] = 0

n, res = int(input()), 0
list = [int(i) for i in input().split()]
for i in list:
    if a[i] == 0:
        tmp = min([abs(i - j) for j in p])
        res = max(res, tmp)
print(res)
