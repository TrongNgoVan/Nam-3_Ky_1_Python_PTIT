for t in range(int(input())):
    n, d = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    print(*(a[d:] + a[:d]))
    