map = {}
t, k = [int(i) for i in input().split()]
for __ in range(t):
    s = input().lower();
    for i in range(len(s)):
        if not s[i].isalnum():
            s = s.replace(s[i], ' ')
    for i in s.split():
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
map = sorted(filter(lambda e: e[1] >= k, map.items()), key=lambda e: (-e[1], e[0]))
for i in map:
    print(*i)
