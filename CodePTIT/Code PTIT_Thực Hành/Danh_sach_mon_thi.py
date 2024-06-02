class Subject:
    def __init__(self, id, name, format) -> None:
        self.id = id
        self.name = name
        self.format = format
    def __str__(self) -> str:
        return '{} {} {}'.format(self.id, self.name, self.format)

list = [Subject(input(), input(), input()) for i in range(int(input()))]
list.sort(key=lambda e: e.id)
print(*list, sep='\n')
# 2
# MUL1320
# Nhap mon da phuong tien
# Bai tap lon + Van dap truc tuyen
# BAS1203
# Giai tich 1
# Thi viet + Van dap truc tuyen