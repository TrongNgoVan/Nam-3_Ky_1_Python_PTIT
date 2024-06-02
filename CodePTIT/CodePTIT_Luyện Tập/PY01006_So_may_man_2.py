for i in range(int(input())):
    num = input()
    cou = num.count('4') + num.count('7')
    print("YES" if cou == len(num) else "NO")
