def tester():
    n = int(input())
    a = sorted([int(i) for i in input().split()])
    b = sorted([int(i) for i in input().split()])
    for i in range(n):
        if a[i] > b[i]:    return "NO"
    return "YES"

for t in range(int(input())):
    print(tester())
