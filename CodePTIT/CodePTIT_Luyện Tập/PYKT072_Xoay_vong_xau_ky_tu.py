res, n, isValid = 1e9, int(input()), True
list = [input() for i in range(n)]

for s0 in list:
    for i in range(len(s0)):
        d = 0
        for j in list:
            s = j
            for k in range(len(j)):
                if s0 == s:
                    d += k
                    break
                s = s[1:] + s[0]
            if s0 != s:
                isValid = False
        res = min(res, d)

print(-1 if isValid == False else res)