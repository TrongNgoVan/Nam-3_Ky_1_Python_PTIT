def test_case():
    n = int(input())
    a = list(map(int, input().split()))
    l, r = [0] * n, [0] * n
    l[0], r[-1] = a[0], a[-1]
    for i in range(1, n):
        l[i] = max(l[i-1], a[i])
    for i in range(n-2, -1, -1):
        r[i] = min(r[i+1], a[i])
    
    res = len([a[i] for i in range(1, n-1) if  l[i-1] <= a[i] and r[i+1] > a[i]])
    if a[0] < r[1]: res += 1
    if a[-1] >= l[-2]:  res += 1
    print(res)

for __ in range(int(input())):
    test_case()