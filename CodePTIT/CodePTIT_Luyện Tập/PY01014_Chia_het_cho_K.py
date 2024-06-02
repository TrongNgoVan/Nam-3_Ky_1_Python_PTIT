a, k, n = [int(i) for i in input().split()]
left = (int(a/k) + 1) * k - a
right = int(n/k) * k - a
if left > right:
    print(-1)
else:
    for i in range(left, right + 1, k):
        print(i, end=' ')