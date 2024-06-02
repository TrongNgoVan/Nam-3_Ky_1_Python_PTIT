import re


list = []
for __ in range(int(input())):
    list += [int(i) for i in re.findall('\\d+', input())]
print(*sorted(list, key=lambda e: e), sep='\n')