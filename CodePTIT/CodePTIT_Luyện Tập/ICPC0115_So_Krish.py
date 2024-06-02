from math import factorial


factorial = {0:1, 1: 1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880}
for t in range(int(input())):
    n = input()
    print("Yes" if int(n) == sum(factorial[int(i)] for i in n) else "No")