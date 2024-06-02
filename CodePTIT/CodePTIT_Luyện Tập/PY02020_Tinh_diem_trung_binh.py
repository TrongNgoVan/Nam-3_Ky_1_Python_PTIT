n = int(input())
a = [float(i) for i in input().split()]
MIN, MAX = min(a), max(a)
s, length = 0, 0
for i in a:
    if i != MIN and i != MAX:
        s += i;
        length += 1
print('{:.2f}'.format(s/length))