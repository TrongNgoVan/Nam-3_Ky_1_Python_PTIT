from math import gcd


class PS:
    def __init__(self, tu, mau) -> None:
        __gcd = gcd(tu, mau)
        self.tu = int(tu/__gcd)
        self.mau = int(mau/__gcd)
    def __str__(self) -> str:
        return f'{self.tu}/{self.mau}'

tu, mau = [int(i) for i in input().split()]
print(PS(tu, mau))