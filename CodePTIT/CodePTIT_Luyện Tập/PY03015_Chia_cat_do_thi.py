n, m, vs, a = 0, 0, [], []

def BFS (s):
    vs[s] = True
    q = [s]
    while q:
        u = q[0]
        q.pop(0)
        for v in a[u]:
            if vs[v] == False:
                vs[v] = True
                q.append(v)

def soTPLT (t):
    global vs
    vs = [False for i in range(n+1)]  
    vs[t] = True
    count = 0
    for i in range(1, n+1):
        if vs[i] == False:
            count += 1
            BFS(i)
    return count


def test_case ():
    global n, m, a
    n, m = [int(i) for i in input().split()]
    a = [[] for i in range(n+1)]
    for __ in range(m):
        u, v = [int(i) for i in input().split()]
        a[u].append(v)
        a[v].append(u)
    max, res = 1, 0
    for i in range(1, n+1):
        tplt = soTPLT(i)
        if tplt > max:
            max = tplt
            res = i
    print(res)    

for __ in range(int(input())):
    test_case()