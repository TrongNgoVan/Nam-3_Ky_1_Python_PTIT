def isValid (n):
    s = 0
    fac = 1
    flag = True
    for index, val in enumerate(n):
        if not index % 2:
            s += int(val)
        else:
            if int(val):
                flag = False
                fac *= int(val)
    if flag: 
        fac = 0
    print(s, fac, sep=' ')

for t in range(int(input())):
    isValid(input())
