from itertools import combinations


n, k = [int(i) for i in input().split()]
a = sorted({str(i) for i in input().split()})
for i in list(combinations(a, k)):
    print(*i)
