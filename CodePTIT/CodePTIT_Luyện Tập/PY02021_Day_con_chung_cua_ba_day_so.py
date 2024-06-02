# def intersection (l1, l2):
#     return [i for i in l1 if i in set(l2)]

def intersection (a, b, c):
    i1, i2, i3, exist = 0, 0 , 0, False
    while (i1 < n and i2 < m and i3 < k):
        if a[i1] == b[i2] and b[i2] == c[i3]:
            print(a[i1], end=' ')
            i1 += 1
            i2 += 1
            i3 += 1
            exist = True
        elif a[i1] < b[i2]: i1 += 1
        elif b[i2] < c[i3]: i2 += 1
        elif c[i3] < a[i1]: i3 += 1
    print('' if exist else 'NO')

for t in range(int(input())):
    n, m, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    intersection(a, b, c)
    