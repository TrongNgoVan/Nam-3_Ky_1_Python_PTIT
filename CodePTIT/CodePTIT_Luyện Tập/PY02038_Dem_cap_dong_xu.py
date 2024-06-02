n, a, res = int(input()), [], 0
for i in range(n):
    a += [[j for j in input()]]
for i in range(n):
    for j in range(n):
        for k in range(j+1, n):
            if a[i][j] == a[i][k] == 'C':   res += 1
            if a[j][i] == a[k][i] == 'C':   res += 1
print(res)