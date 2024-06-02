def isValid (n):
    for i in range(2, len(n), 2):
        if n[i] != n[i-2]:
            return False
    return len(n) % 2 and n[0] != n[1]

for t in range(int(input())):
    print("YES" if isValid(input()) else "NO")