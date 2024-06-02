def BFS (a, n, u, vs, prev):
    for v in range(1, n+1):
        if a[u][v] == 1 and vs[v] == 0:
            vs[v] = 1
            prev[v] = u
            BFS (a, n, v, vs, prev)


def test_case():
    n, m, u, v = [int(i) for i in input().split()]
    a = [[0 for j in range(n+1)] for i in range(n+1)]
    vs, prev = [0 for i in range(n+1)], [0 for i in range(n+1)]
    for __ in range(m):
        i, j = [int(k) for k in input().split()]
        a[i][j] = 1

    res = 0
    for i in range(1, n+1):
        if i != u and i != v:
            vs[i] = 1
            BFS(a, n, u, vs, prev)
            if prev[v] == 0:
                res += 1
            vs, prev = [0 for i in range(n+1)], [0 for i in range(n+1)]

    print(res)

for __ in range(int(input())):
    test_case()