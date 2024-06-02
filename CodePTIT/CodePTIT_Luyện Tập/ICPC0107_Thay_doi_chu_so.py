for t in range(int(input())):
    p, q = [str(i) for i in input().split()]
    arr = input().split()
    if len(arr) == 1:
        x1 = arr[0]
        x2 = input()
    else:
        x1, x2 = arr
    print(int(x1.replace(max(p, q), min(p, q))) + int(x2.replace(max(p, q), min(p, q))), int(x1.replace(min(p, q), max(p, q))) + int(x2.replace(min(p, q), max(p, q))), sep=' ')