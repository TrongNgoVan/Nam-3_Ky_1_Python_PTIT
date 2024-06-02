n = int(input())
a = [int(i) for i in input().split()]
step, res = 1e6, 1e6
for i in a:
    s = sum(abs(i - j) for j in a)
    if s < step:
        step = s
        res = i
print(step, res, sep=' ')