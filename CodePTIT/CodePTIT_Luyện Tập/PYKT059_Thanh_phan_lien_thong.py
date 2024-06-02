n, m, x = [int(i) for i in input().split()]
vs = [0] * (n+1)
a = [[] for i in range(n+1)]

for __ in range(m):
    i, j = [int(i) for i in input().split()]
    a[i].append(j)
    a[j].append(i)


def BFS (x):
    queue = []
    queue.append(x)
    vs[x] = 1
    while len(queue) > 0:
        u = queue[0]
        queue.pop(0)
        if len(a[u]) > 0:
            for v in a[u]:
                if vs[v] == 0:
                    queue.append(v)
                    vs[v] = 1

BFS(x)
res = [i for i in range(1, n+1) if vs[i] == 0]
print(* 0 if len(res) == 0 else res, sep='\n')