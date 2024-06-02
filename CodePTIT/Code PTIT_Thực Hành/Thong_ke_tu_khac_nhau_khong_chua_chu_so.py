map = {}
for t in range(int(input())):
    s = input().lower();
    for i in range(len(s)):
        if not s[i].isalpha():
            s = s.replace(s[i], ' ')
    for i in s.split():
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
map = sorted(map.items(), key=lambda e: (-e[1], e[0]))
for i in map:
    print(*i)
