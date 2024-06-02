n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
above = under = 0
for i in range(n):
    for j in range(n):
        if j > i:   above += a[i][j]
        elif j < i: under += a[i][j]
print("YES" if abs(above - under) <= int(input()) else "NO")
print(abs(above - under))
