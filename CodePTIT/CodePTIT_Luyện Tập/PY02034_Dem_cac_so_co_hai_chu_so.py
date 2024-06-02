dict, s = {}, input()
for i in range(0, len(s)-1, 2):
    tmp = s[i:i+2]
    if tmp not in dict.keys():
        dict[tmp] = 1
    else:   dict[tmp] += 1
for k, v in dict.items():
    print(k, v)