for __ in range(int(input())):
    n, p = [int(i) for i in input().split()]
    res = 0
    for i in range(p, n+1, p):
        tmp = i
        while tmp%p == 0:
            tmp /= p
            res += 1
    print(res)