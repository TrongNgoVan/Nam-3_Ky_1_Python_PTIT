class Department:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name

class Staff:
    def __init__(self, id, name, basicSalary, workDays, department) -> None:
        self.id = id
        self.name = name
        self.basicSalary = basicSalary
        self.workDays = workDays
        self.department = department
    def getFactor(self):
        group, years = self.id[0], int(self.id[1:3])
        if group == 'A':
            if years >= 1 and years <= 3:   return 10
            if years >= 4 and years <= 8:   return 12
            if years >= 9 and years <= 15:   return 14
            if years >= 16:   return 20
        elif group == 'B':
            if years >= 1 and years <= 3:   return 10
            if years >= 4 and years <= 8:   return 11
            if years >= 9 and years <= 15:   return 13
            if years >= 16:   return 16
        elif group == 'C':
            if years >= 1 and years <= 3:   return 9
            if years >= 4 and years <= 8:   return 10
            if years >= 9 and years <= 15:   return 12
            if years >= 16:   return 14
        elif group == 'D':
            if years >= 1 and years <= 3:   return 8
            if years >= 4 and years <= 8:   return 9
            if years >= 9 and years <= 15:   return 11
            if years >= 16:   return 13
        return 0
    def getSalary(self):
        return self.basicSalary * self.workDays * self.getFactor()
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.department.name} {self.getSalary()*1000}'

departments = []
for i in range(int(input())):
    s = input()
    departments.append(Department(s[:2], s[3:]))

staffs = []
for i in range(int(input())):
    id = input()
    deId = id[-2:]
    for de in departments:
        if de.id == deId:
            staffs.append(Staff(id, input(), int(input()), int(input()), de))
            break

print(*staffs, sep='\n')