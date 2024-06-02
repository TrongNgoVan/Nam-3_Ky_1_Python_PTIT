for t in range(int(input())):
    n, m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    a.insert(a.index(max(a)), m)
    print(*list(filter(lambda x: x < 0, a)), *list(filter(lambda x: x >= 0, a)))