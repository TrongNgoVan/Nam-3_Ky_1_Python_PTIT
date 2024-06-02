def solve (a, b, n):
    for i in range(n):
        if a[i] > b[i]: return False
    return True
for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    print("YES" if solve(a, b, n) else "NO")
