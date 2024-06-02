class Subject:
    def __init__(self, id, name, format) -> None:
        self.id = id
        self.name = name
        self.format = format
    def __str__(self) -> str:
        return self.id + " " + self.name + " " + self.format

list = []
for __ in range(int(input())):
    list.append(Subject(input(), input(), input()))
print(*sorted(list, key=lambda e: e.id), sep='\n')