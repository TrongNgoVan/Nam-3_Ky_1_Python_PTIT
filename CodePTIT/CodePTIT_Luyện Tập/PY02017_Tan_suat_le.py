for t in range(int(input())):
    n = int(input())
    m = dict()
    a = [int(i) for i in input().split()]
    for i in a:
        if i in m:  m[i] += 1
        else:   m[i] = 1
    for i in a:
        if m[i] % 2:
            print(i)
            break