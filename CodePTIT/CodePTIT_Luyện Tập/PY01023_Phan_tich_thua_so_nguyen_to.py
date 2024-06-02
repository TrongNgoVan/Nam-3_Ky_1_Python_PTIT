from math import sqrt
from tracemalloc import start


def analyze (n):
    res = {}
    for i in range (2, int(sqrt(n)) + 1):
        cou = 0
        if not n%i:
            while not n%i:
                n = int(n/i)
                cou += 1
            res.update({i: cou})
    if n > 1:
        res.update({n: 1})
    print('1', end='')
    for i in res:
        print(" * {}^{}".format(i, res[i]), end='')
    print()

for t in range(int(input())):
    n = int(input())
    analyze(n)