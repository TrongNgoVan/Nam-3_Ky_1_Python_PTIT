for t in range(int(input())):
    n = int(input())
    a = {int(i) for i in input().split()}
    print(max(a) - min(a) + 1 - len(a))