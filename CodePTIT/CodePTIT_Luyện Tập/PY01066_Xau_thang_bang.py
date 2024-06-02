def isBalanced (a):
    b = a[::-1]
    for i in range(1, len(a)):
        if abs(ord(a[i]) - ord(a[i-1])) != abs(ord(b[i]) - ord(b[i-1])):
            return False
    return True

for t in range(int(input())):
    print("YES" if isBalanced(input()) else "NO")