from math import ceil, log


def test_case ():
    n, x, m = [float(i) for i in input().split()]
    x /= 100
    res = ceil(log(m / n, x + 1))
    print(res)

for t in range(int(input())):
    test_case()