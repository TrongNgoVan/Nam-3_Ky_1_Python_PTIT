def solve ():
    s = input()
    s += ' '
    cou = 0
    res = ''
    for i in range(len(s)):
        if i == 0 or s[i] == s[i-1]:    cou += 1
        elif s[i] != s[i-1]:
            res += str(cou) + s[i-1]
            cou = 1
    print(res)

for t in range (int(input())):
    solve()