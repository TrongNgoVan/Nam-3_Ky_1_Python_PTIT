a = []
while len(a) < 10:
    a.extend(input().split())
print(len({int(x)%42 for x in a}))