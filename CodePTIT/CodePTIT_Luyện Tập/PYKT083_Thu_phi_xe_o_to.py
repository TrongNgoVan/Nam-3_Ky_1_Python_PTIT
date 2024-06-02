def getPrice (s):
    if s[3] == 'OUT':   return 0
    if s[1] == 'Xe_con' and int(s[2]) == 5:    return 10000
    if s[1] == 'Xe_con' and int(s[2]) == 7:    return 15000
    if s[1] == 'Xe_tai' and int(s[2]) == 2:    return 20000
    if s[1] == 'Xe_khach' and int(s[2]) == 29:    return 50000
    if s[1] == 'Xe_khach' and int(s[2]) == 45:    return 70000

dict = {}
for t in range(int(input())):
    s = [i for i in input().split()]
    if dict.get(s[-1]) == None:
        dict.update({s[-1] : getPrice(s)})
    else: dict.update({s[-1] : dict[s[-1]] + getPrice(s)})
for k, v in dict.items():
    print(k, v, sep=': ')