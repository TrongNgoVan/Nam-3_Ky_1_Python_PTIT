n, m = [int(i) for i in input().split()]
a = [[int(i) for i in input().split()] for j in range(n)]
res = max(a[i][j] for i in range(n) for j in range(m)) - min(a[i][j] for i in range(n) for j in range(m))
arr = [f'Vi tri [{i}][{j}]' for i in range(n) for j in range(m) if a[i][j] == res]
print(res, *arr , sep='\n') if arr else print('NOT FOUND')