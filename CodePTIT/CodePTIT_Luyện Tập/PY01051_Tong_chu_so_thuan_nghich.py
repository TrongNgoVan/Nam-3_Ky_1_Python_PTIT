def isReversible (s):
    return s == s[::-1] and len(s) > 1

for t in range(int(input())):
    print("YES" if isReversible(str(sum(int(i) for i in input()))) else "NO")