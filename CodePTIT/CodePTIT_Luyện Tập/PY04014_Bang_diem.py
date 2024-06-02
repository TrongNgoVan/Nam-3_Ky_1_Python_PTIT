class Student:
    def __init__(self, id, name, *list):
        self.id = id
        self.name = name
        self.score = float('{:.1f}'.format((sum(float(i) for i in list)+float(list[0]) + float(list[1]))/10/1.2))
        if self.score >= 9:
            self.hl = "XUAT SAC"
        elif self.score >= 8:
            self.hl = "GIOI"
        elif self.score >= 7:
            self.hl = "KHA"
        elif self.score >= 5:
            self.hl = "TB"
        else: self.hl = "YEU"
    
    def __str__(self):
        return self.id + " " + self.name + " " + str(self.score) + " " + self.hl

list = [Student('HS{0:0>2}'.format(i+1), input(), *input().split()) for i in range(int(input()))]
list.sort(key=lambda ele: (-ele.score, ele.id))
print(*list, sep='\n')