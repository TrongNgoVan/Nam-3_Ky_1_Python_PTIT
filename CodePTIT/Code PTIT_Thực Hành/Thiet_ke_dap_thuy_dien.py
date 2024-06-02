import re
from bisect import bisect_left
from sys import stdin

# test cho input như cdb :))
list = iter([int(i) for i in re.split('\\s+', ' '.join(stdin.readlines()).strip())])

for __ in range(next(list)):
    n = next(list) # so luong dap
    p = [next(list) for i in range(n)] # vi tri dap thu i
    h = [next(list) for i in range(n)] # chieu cao cua dap thu i

    stack = []
    higher = [] # vi tri dap dau tien ben trai cao hon dap thu i
    for i in range(n):
        while stack and h[i] >= h[stack[-1]]:
            stack.pop()
        higher.append(-1 if not stack else stack[-1])
        stack.append(i)

    sum = [0] * n   # tong the tich cac dap truoc i
    for i in range(1, n):
        sum[i] = sum[i-1] + h[i-1]

    v = [0] * n  # the tich lon nhat co the chua den dap thu i
    for i in range(n):
        v[i] = v[higher[i]] + (p[i] - 1 - p[higher[i]]) * h[i] - (sum[i] - sum[higher[i]+1]) if higher[i] != -1 else p[i] * h[i] - sum[i]

    for q in range(next(list)):
        k = next(list)
        res = 0
        print(bisect_left(v, k, 0, n))
        