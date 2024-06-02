from math import log


f = open('DATA.in', 'r')

s = '0123456789ABCDEFG'
for __ in range(int(next(f))):
    n = int(log(int(next(f)), 2))
    num = next(f).strip()[::-1]
    print(*[s[int(num[i:i+n][::-1], 2)] for i in range(0, len(num), n)][::-1], sep='')

# Cach 2
# s = '0123456789ABCDEF'
# with open('DATA.in', 'r') as f:
#     t = int(f.readline())
#     for __ in range(t):
#         n = int(f.readline())
#         num = int(f.readline(), 2)
#         res = ''
#         while num:
#             res += s[num%n]
#             num //= n
#         print(res[::-1])