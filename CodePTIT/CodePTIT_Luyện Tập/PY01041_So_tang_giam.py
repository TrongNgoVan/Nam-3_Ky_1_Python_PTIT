def isValid (n):
    if len(s) < 3:
        return False
    i = 1
    while i < len(s) and n[i] > n[i-1]:
        i += 1
    while i < len(s) and n[i] < n[i-1]:
        i += 1
    return i == len(n)

for t in range(int(input())):
    s = input()
    print("YES" if isValid(s) else "NO")