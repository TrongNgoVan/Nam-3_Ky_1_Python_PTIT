class Staff:
    def __init__(self, stt, name, score1, score2) -> None:
        self.name = name
        self.id = 'TS0' + str(stt)
        while score1 > 10:
            score1 /= 10
        while score2 > 10:
            score2 /= 10
        self.score = (score1 + score2) / 2
    def getStatus(self):
        if (self.score < 5) :   return 'TRUOT'
        if (self.score < 8) :   return 'CAN NHAC'
        if (self.score <= 9.5) :   return 'DAT'
        else:   return "XUAT SAC"
    def __str__(self) -> str:
        return self.id + ' ' + self.name + ' ' + '{:.2f}'.format(self.score) + ' ' + self.getStatus()


staff = [Staff(t+1, input(), float(input()), float(input())) for t in range(int(input()))]
staff.sort(key=lambda e: -e.score)
print(*staff, sep='\n')
# 3
# Nguyen Thai Binh
# 45
# 75
# Le Cong Hoa
# 4
# 4.5
# Phan Van Duc
# 56
# 56