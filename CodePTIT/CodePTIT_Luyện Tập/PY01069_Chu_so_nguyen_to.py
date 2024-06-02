p = '2357'
list = []

def isValid(s):
    for i in p:
        if s.count(i) == 0:
            return False
    return s[-1] != '2'

def backtrack (i, s, n):
    if i >= 4 and i <= n and isValid(s):
        list.append(int(s))
    if i < n:
        for c in p:
            backtrack(i+1, s + c, n)

backtrack(0, '', int(input()))
print(*sorted(list), sep='\n')