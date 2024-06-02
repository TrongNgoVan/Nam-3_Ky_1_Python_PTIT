from datetime import datetime


class Biker:
    def __init__(self, name, unit, endTime) -> None:
        self.name = name
        self.unit = unit
        self.id = self.getId(name, unit)
        time = datetime.strptime(endTime, '%H:%M')  - datetime.strptime('6:00', '%H:%M')
        self.speed = 120 / time.seconds * 3600
    def getId (self, name, unit) -> str:
        return ''.join([i[0:1].upper() for i in unit.split()]) + ''.join([i[0:1].upper() for i in name.split()])
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.unit} {round(self.speed)} Km/h'

list = []
for __ in range(int(input())):
    list.append(Biker(input(), input(), input()))
print(*sorted(list, key= lambda e: -e.speed), sep='\n')