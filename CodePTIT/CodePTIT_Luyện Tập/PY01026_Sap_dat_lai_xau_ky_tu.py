for t in range(int(input())):
    print("Test " + str(t+1) + ": " + ("YES" if ''.join(sorted(input())) == ''.join(sorted(input())) else "NO"))