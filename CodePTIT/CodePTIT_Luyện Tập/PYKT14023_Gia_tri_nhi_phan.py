import heapq

n, m = [int(i) for i in input().split()]
a = [[] for i in range(n+1)]

p_queue = []
heapq.heapify(p_queue)

for __ in range(m):
    i, j = sorted([int(i) for i in input().split()])
    a[i].append(j)

for i in range(1, n+1):
    for j in a[i]:  heapq.heappush(p_queue, j)
    print(len(p_queue)%2, end=' ')
    while p_queue and i == p_queue[0]:  heapq.heappop(p_queue)
