from math import log


def test_case():
    n, res = int(input()), 0
    a = [int(i) for i in input().split()]
    for i in range(1, n):
        lower, greater = min(a[i], a[i-1]), max(a[i], a[i-1])
        if greater > lower * 2:
            div = log(greater / lower, 2)
            res += int(div) if div != int(div) else int(div) - 1
    print(res)

for __ in range(int(input())):
    test_case()