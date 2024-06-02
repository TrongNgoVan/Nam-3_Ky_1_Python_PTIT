import re


for t in range(int(input())):
    n = int(input())
    i = 2
    num = int(str(i) + str(i)[::-1])
    while num < n:
        if not len(re.findall("[13579]+", str(i))):
            print(num, end=' ')
        i += 2
        num = int(str(i) + str(i)[::-1])
    print()
