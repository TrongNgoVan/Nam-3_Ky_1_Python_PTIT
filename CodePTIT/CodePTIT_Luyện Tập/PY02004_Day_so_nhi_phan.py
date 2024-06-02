n = input()
res = 0
a = [int(j) for j in input().split()]
for i in range(1, len(a)):
    if a[i] != a[i-1]:
        res += 1
print(res)
