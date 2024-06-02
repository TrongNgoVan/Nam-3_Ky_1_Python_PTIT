def multi (arg):
    res = 1
    for i in arg:
        res *= int(i)
    return res

for t in range(int(input())):
    n = input()
    a = [i for i in input().split()]
    print(*sorted(a, key=lambda ele: (multi(ele), int(ele))))
