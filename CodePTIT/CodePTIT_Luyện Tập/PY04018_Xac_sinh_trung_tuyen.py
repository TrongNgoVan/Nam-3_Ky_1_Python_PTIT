class GV:
    def __init__(self, i, name, code, score1, score2) -> None:
        self.name = name
        self.id = 'GV{:02d}'.format(i)
        self.total = score1*2 + score2 + self.getPriority(code)
        self.sj = self.getSubject(code)
    def getSubject(self, code):
        if code[0] == 'A':  return 'TOAN'
        if code[0] == 'B':  return 'LY'
        return 'HOA'
    def getPriority(self, code):
        if code[1] == '1':  return 2
        if code[1] == '2':  return 1.5
        if code[1] == '3':  return 1
        return 0
    def getStatus(self):
        return "TRUNG TUYEN" if self.total >= 18 else "LOAI"
    def __str__(self) -> str:
        return '{:s} {:s} {:s} {:.1f} {:s}'.format(self.id, self.name, self.sj, self.total, self.getStatus())

list = []
for i in range(int(input())):
    list.append(GV(i+1, input(), input(), float(input()), float(input())))
print(*sorted(list, key=lambda e: -e.total), sep='\n')
        
