class SV:
    def __init__(self, id, name, classId) -> None:
        self.id = id
        self.name = name
        self.classId = classId
    def getScore(self, s) -> None:
        res = 10 - s.count('v')*2 - s.count('m')
        self.status = '0 KDDK' if res <= 0 else res
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.classId} {self.status}'

n, list = int(input()), []
for __ in range(n):
    list.append(SV(input(), input(), input()))
for __ in range(n):
    id, s = [i for i in input().split()]
    for i in list:
        if i.id == id:
            i.getScore(s)
            break
print(*list, sep='\n')