alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for t in range(int(input())):
    n, base = [int(i) for i in input().split()]
    ans = ''
    while n:
        ans += alpha[n%base]
        n //= base
    print(ans[::-1])