n = int(input())
a = [int(j) for j in input().split()]
for i in range(1, n+2):
    if not i in a:
        print(i)
        break