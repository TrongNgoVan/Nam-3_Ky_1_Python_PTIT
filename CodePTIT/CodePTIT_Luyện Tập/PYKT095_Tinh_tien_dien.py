class Client:
    def __init__(self, id, name, type, start, end) -> None:
        self.id = 'KH{:02d}'.format(id)
        self.name = self.nameFormat(name)
        self.standard = self.getStandard(type)
        self.num = end - start
    def getStandard (self, type):
        if type == 'A': return 100
        elif type == 'B':   return 500
        elif type == 'C':   return 200
        return 0
    def getBelowStandard (self):
        return min(self.num, self.standard) * 450
    def getAboveStandard(self):
        diff = self.num - self.standard
        return 0 if diff <= 0 else diff * 1000
    def getVAT(self):
        return self.getAboveStandard() // 20
    def getTotal(self):
        return self.getAboveStandard() + self.getBelowStandard() + self.getVAT()
    def nameFormat (self, name):
        s = name.strip().split()
        return ' '.join(i.capitalize() for i in s)
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.getBelowStandard()} {self.getAboveStandard()} {self.getVAT()} {self.getTotal()}'
    
list = []
for i in range(int(input())):
    name, s = input(), input().split()
    list.append(Client(i+1, name, s[0], int(s[1]), int(s[2])))
print(*sorted(list, key=lambda e: -e.getTotal()), sep='\n')