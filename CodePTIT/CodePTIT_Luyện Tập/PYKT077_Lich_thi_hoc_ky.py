from datetime import datetime


class Subject:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
    def __str__(self) -> str:
        return f'{self.id} {self.name}'

class Schedule:
    def __init__(self, id, sj, date, time, group) -> None:
        self.id = 'T{:03d}'.format(id)
        self.sj = sj
        self.date = date
        self.time = time
        self.group = group
    def __str__(self) -> str:
        return f'{self.id} {str(self.sj)} {self.date} {self.time} {self.group}'

n, m = [int(i) for i in input().split()]
subjects = [Subject(input(), input()) for i in range(n)]
schedules = []
for i in range(m):
    s = input().split()
    sjId = s[0]
    for sj in subjects:
        if sj.id == sjId:
            schedules.append(Schedule(i+1, sj, s[1], s[2], s[3]))
            break
schedules.sort(key=lambda e: (datetime.strptime(e.date, '%d/%m/%Y'), datetime.strptime(e.time, '%H:%M'), e.id))
print(*schedules, sep='\n')