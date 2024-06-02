class Student:
    def __init__(self, name, *arg) -> None:
        self.name = name
        self.correct = int(arg[0])
        self.submit = int(arg[1])
    def __str__(self):
        return self.name + " " + str(self.correct) + " " + str(self.submit)
    
n = int(input())
list = []
for i in range(n):
    list += [Student(input(), *input().split())]
list.sort(key=lambda ele: (-ele.correct, ele.submit, ele.name))
print(*list, sep='\n')