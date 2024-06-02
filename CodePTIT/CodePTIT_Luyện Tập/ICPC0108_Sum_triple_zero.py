for t in range(int(input())):
    n, res = int(input()), 0
    a = sorted([int(i) for i in input().split()])
    for i in range(n-2):
        l, r = i+1, n-1
        while l < r:
            tmp = a[i] + a[l] + a[r]
            if not tmp:
                res += 1
                l += 1
            elif tmp < 0:
                l += 1
            else:
                r -= 1
    print(res)