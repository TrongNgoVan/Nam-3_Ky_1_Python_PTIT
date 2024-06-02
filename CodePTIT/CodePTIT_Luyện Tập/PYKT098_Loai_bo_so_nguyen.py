import sys


line = open('DATA.in', 'r')
list = []
for i in line:
    list += [i for i in i.split() if not i.isdigit() or int(i) > sys.maxsize]
print(*sorted(list, key=lambda e: e))