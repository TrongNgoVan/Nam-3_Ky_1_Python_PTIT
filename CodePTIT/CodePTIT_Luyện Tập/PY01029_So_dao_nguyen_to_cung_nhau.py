from math import gcd
for t in range(int(input())):
    n = input()
    m = n[::-1]
    print("YES" if gcd(int(n), int(m)) == 1 else "NO")