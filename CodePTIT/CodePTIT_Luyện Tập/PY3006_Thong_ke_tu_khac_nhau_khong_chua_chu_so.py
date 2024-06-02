import re


map = {}
for t in range(int(input())):
    s = input().lower();
    for i in range(len(s)):
        if not s[i].isalnum():
            s = s.replace(s[i], ' ')
    for i in s.split():
        if re.findall('\d', i):  
            i = re.sub('\d+', '', i)
        if i == '': continue
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
map = sorted(map.items(), key=lambda e: (-e[1], e[0]))
for i in map:
    print(*i)
