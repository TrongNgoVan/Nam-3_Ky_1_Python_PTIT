def solution ():
    s = input()
    print( "YES" if s[:2] == s[-2:] else "NO")
for i in range(int(input())):
    solution()