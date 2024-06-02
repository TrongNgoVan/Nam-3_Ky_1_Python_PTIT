n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
discount = [a[i] - b[i] for i in range(n)]
a = sorted(zip(a, b, discount), key= lambda e: e[2])
print(sum(i for i, j, k in a[:k]) + sum((j if i > j else i) for i, j, k in a[k:]))
