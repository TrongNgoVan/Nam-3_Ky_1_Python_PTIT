for __ in range(int(input())):
    n, m = [int(i) for i in input().split()]
    x = [[int(j) for j in input().split()] for i in range(n)]
    h = [[int(j) for j in input().split()] for i in range(3)]

    # y = [[0] * (m-2) for i in range(n-2)]
    # for i in range(n-2):
    #     for j in range(m-2):
    #         y[i][j] = sum(h[k][l] * x[i+k][j+l] for l in range(3) for k in range(3))
    y = [[sum(h[k][l] * x[i+k][j+l] for l in range(3) for k in range(3)) for j in range(m-2)] for i in range(n-2)]
    print(sum([sum(i) for i in y]))