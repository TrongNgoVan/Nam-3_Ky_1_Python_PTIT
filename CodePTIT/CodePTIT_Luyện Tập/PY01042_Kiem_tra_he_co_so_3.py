def isValid (n):
    return n.count('0') + n.count('1') + n.count('2') == len(n)
for t in range(int(input())):
    n = input()
    print("YES" if isValid(n) else "NO")