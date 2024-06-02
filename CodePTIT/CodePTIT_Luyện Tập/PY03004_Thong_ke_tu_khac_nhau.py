map = {}
for t in range(int(input())):
    s = input().lower();
    for i in range(len(s)):
        if not s[i].isalnum():
            s = s.replace(s[i], ' ')
    for i in s.split():
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
map = sorted(map.items(), key=lambda e: (-e[1], e[0]))
for i in map:
    print(*i)

# Cach 2
# from sys import stdin
# import re

# dict = {}
# for __ in range(int(stdin.readline())):
#     s = re.findall('[\\w\\d]+', stdin.readline().lower())
#     for i in s:
#         dict[i] = dict[i] + 1 if i in dict else 1
    
# for i in sorted(dict.items(), key=lambda e: (-e[1], e[0])):
#     print(*i)