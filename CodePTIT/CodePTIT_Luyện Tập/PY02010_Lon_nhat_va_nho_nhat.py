n = int(input())
while n:
    a = [int(input()) for i in range(n)]
    print("BANG NHAU" if a.count(a[0]) == n else f'{min(a)} {max(a)}')
    n = int(input())