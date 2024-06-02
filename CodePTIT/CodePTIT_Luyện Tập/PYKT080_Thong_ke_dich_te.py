n, m = [int(i) for i in input().split()]
res = 0

move_i = [-1, -1, -1, 0, 0, 1, 1, 1]
move_j = [-1, 0, 1, -1, 1, -1, 0, 1]

vs = [[False for j in range(m+2)] for i in range(n+2)]
a = [[0]*(m+2)]
for i in range(n):
    a += [[0] + [int(i) for i in input().split()] + [0]]
a += [[0]*(m+2)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i][j] == -1:
            for k in range(8):
                if not vs[i+move_i[k]][j+move_j[k]]:
                    res += a[i+move_i[k]][j+move_j[k]]
                    vs[i+move_i[k]][j+move_j[k]] = True
print(res)