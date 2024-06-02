n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]

if n > m:
    a = [a[i] for i in range(n) if not(i % 2 == 0 and i//2 < n-m)]
elif m > n:
    a = [[a[i][j] for j in range(m) if not(j % 2 == 1 and j//2 < m-n)] for i in range(n)]

for i in a:
    print(*i)