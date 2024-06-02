import re

list = []

def backtrack (i, s, n, tuple):
    if s == n:  list.append(re.sub(',', '', str(tuple)))
    elif s < n:
        for j in range(i, 0, -1):
            backtrack(j, s+j, n, (*tuple, j))
        
for __ in range(int(input())):
    list, n = [], int(input())
    backtrack(n, 0, n, ())
    print(len(list))
    print(*list)
