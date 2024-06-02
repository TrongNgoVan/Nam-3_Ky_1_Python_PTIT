n = int(input())
a = []
while len(a) < n:
    a += [int(i) for i in input().split()]
m = [0]*len(a)
even, odd = [], []
for i in range(n):
    if a[i]%2:
        odd += [a[i]]
    else:
        m[i] = 1
        even += [a[i]]
even.sort()
odd.sort(key=lambda ele: -ele)
i, j = 0, 0
for k in range(n):
    if m[k]:
        print(even[i], end=' ')
        i += 1
    else:
        print(odd[j], end=' ')
        j += 1