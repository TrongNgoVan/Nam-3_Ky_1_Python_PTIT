def check():
    n = input()
    return True if (n[-2: ] == '86') else False

for t in range(int(input())):
    print("YES" if check() else "NO")