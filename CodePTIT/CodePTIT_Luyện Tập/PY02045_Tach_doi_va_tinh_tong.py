s = input()
while (len(s) > 1):
    n = int(len(s)/2)
    res = int(s[:n]) + int(s[n:])
    print(res)
    s = str(res)