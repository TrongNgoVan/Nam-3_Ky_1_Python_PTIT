def isValid (n):
    for i in range(1, len(n)):
        if abs(ord(n[i]) - ord(n[i-1])) != 2:
            return False
    return True

for t in range(int(input())):
    n = input()
    print ("YES" if not (sum(int(i) for i in n) % 10) and isValid(n) else "NO")