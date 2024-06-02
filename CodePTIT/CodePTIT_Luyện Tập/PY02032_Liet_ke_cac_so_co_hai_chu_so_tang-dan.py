s = input()
print(*sorted(set([s[i:i+2] for i in range(0, len(s)-2, 2)])))
