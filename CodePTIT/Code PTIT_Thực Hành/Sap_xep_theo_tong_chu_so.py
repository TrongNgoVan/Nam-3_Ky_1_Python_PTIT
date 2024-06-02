for t in range(int(input())):
    n = int(input())
    list = [i for i in input().split()]
    list.sort(key=lambda e: (sum(int(i) for i in e), int(e)))
    print(*list, sep=' ', end='\n')