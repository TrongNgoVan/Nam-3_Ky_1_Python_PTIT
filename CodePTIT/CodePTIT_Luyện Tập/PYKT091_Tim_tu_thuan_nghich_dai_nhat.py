def isReversible(s):
    return s == s[::-1]

res = 0
dict = {}
for line in open('VANBAN.in', 'r'):
    s = line.strip().split()
    for i in s:
        if isReversible(i):
            dict[i] = dict[i] + 1 if i in dict.keys() else 1
            res = max(res, len(i))

for i in [i for i in dict.items() if len(i[0]) == res]:
    print(*i)