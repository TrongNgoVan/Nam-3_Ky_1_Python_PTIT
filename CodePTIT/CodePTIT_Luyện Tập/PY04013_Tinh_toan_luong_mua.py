from datetime import datetime


class Data:
    def __init__(self, stt, name, start, end, amount) -> None:
        self.id = 'T{:02d}'.format(stt)
        self.name = name
        self.time = datetime.strptime(end, "%H:%M") - datetime.strptime(start, "%H:%M")
        self.amount = amount
    def __str__(self) -> str:
        return '{:s} {:s} {:.2f}'.format(self.id, self.name, self.amount * 3600 / self.time.seconds)

list = []

def isInList(data):
    for i in list:
        if i.name == data.name:
            i.amount += data.amount
            i.time += data.time
            return
    list.append(data)

for t in range(1, int(input()) + 1):
    data = Data(t, input(), input(), input(), int(input()))
    isInList(data)

print(*list, sep='\n')