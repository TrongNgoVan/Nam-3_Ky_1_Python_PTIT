n = input()
res = 0
while len(n) > 1:
    n = str(sum((ord(i) - ord('0')) for i in n))
    res += 1
print(res)