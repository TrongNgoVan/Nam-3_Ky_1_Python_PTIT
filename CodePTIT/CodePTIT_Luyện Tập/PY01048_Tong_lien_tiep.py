# n = a + (a + 1) + (a + 2) + ... + (a + b) = (b + 1) * (a + b/2)
# => 2n = (b + 1) * (2a + b) là tích 2 số tự nhiên với b + 1 < 2a + b và khác tính chẵn lẻ
# => duyệt các ước của 2n = c * (2a + c - 1)

from math import sqrt


for __ in range(int(input())):
    n = int(input()) * 2
    print(len([i for i in range(2, int(sqrt(n)) + 1) if n%i == 0 and (n//i-i)&1 == 1]))
