from itertools import permutations

for __ in range(int(input())):
    a = list(permutations(range(1, int(input()) + 1)))
    print(len(a))
    for i in a[::-1]:
        print(*i, sep='', end=' ')
    print()