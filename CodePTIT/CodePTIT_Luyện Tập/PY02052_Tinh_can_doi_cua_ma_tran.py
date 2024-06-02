n, low, up = int(input()), 0, 0
a = []
for t in range(n):
    a += [[int(i) for i in input().split()]]
for i in range(n):
    for j in range(n):
        if i > j:   low += a[i][j]
        elif i < j: up += a[i][j]
res = abs(low - up)
print("YES" if res <= int(input()) else "NO")
print(res)