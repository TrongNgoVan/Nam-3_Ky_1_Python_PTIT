from datetime import datetime

class Bill:
    def __init__(self, i, name, room, arrival, departure, serveFee) -> None:
        self.id = 'KH{:02d}'.format(i)
        self.name = name
        self.room = room
        time = datetime.strptime(departure, '%d/%m/%Y') - datetime.strptime(arrival, '%d/%m/%Y') 
        self.days = time.days + 1
        self.serveFee = serveFee
    def totalFee (self) -> int:
        if self.room[0] == '1': return 25 * self.days + self.serveFee
        if self.room[0] == '2': return 34 * self.days + self.serveFee
        if self.room[0] == '3': return 50 * self.days + self.serveFee
        if self.room[0] == '4': return 80 * self.days + self.serveFee
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.room} {self.days} {self.totalFee()}'

list = []
for i in range(1, int(input()) + 1):
    list.append(Bill(i, input().strip(), input().strip(), input().strip(), input().strip(), int(input().strip())))
print(*sorted(list, key= lambda e: -e.totalFee()), sep='\n')