for t in range(int(input())):
    n = int(input())
    a = [i for i in input().split()]
    print(*sorted(a, key=lambda ele: (sum(int(i) for i in ele), int(ele))))