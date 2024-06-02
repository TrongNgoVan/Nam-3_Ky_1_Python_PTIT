def check(s):
    for i in range(0, len(s)-1):
        if s[i] > s[i+1]:   return False
    return True
t = int(input())
for j in range(0, t):
    s = input()
    print("YES" if check(s) else "NO")
