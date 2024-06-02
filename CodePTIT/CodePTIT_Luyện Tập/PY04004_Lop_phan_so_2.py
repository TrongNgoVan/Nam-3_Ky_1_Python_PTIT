from math import gcd


class PS:
    def __init__(self, tu, mau) -> None:
        __gcd = gcd(tu, mau)
        self.tu = int(tu/__gcd)
        self.mau = int(mau/__gcd)
    def add(self, other):
        return PS(self.tu * other.mau + self.mau * other.tu, self.mau * other.mau)
    def __str__(self) -> str:
        return f'{self.tu}/{self.mau}'

x1, y1, x2, y2 = [int(i) for i in input().split()]
print(PS(x1, y1).add(PS(x2, y2)))