for t in range(int(input())):
    n = int(input())
    print("{:.6f}".format(sum(float(1/i) for i in range (1 if n%2 else 2, n+1, 2))))