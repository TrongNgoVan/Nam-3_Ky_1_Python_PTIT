n, res = int(input()), 0
list = sorted([int(i) for i in input().split()])
print(max(list[-1]*list[-2], list[-1]*list[-2]*list[-3], list[0]*list[1], list[-1]*list[0]*list[1]))