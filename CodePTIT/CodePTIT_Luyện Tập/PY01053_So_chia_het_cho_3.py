for t in range(int(input())):
    print("YES" if not sum(int(i) for i in input()) % 3 else "NO")