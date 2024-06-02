for t in range(int(input())):
    list = [i for i in input().split()]
    count = 0
    for i in list:
        if count + len(i) > 100:    break
        print(i, end='')
        count += len(i)
        print(end=' ')
        count += 1
    print()