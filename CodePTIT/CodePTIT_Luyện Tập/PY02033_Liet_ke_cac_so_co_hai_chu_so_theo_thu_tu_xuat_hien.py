s, list = input(), []
for i in range(0, len(s)-1, 2):
    if s[i:i+2] not in list:
        list += [s[i:i+2]]
print(*list, sep=' ')