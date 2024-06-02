import itertools


n , k = [int(i) for i in input().split()]
for i in itertools.combinations(sorted({int(i) for i in input().split()}), k):
    print(*i)