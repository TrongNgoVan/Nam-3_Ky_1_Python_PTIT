class Candidate:
    def __init__(self, i, name, score, ethnic, area) -> None:
        self.id = 'TS{:02d}'.format(i)
        self.score = score + self.ethicBonus(ethnic) + self.areaBonus(area)
        self.name = self.formatName(name)
        self.status = 'Do' if self.score >= 20.5 else 'Truot'
    def formatName(self, name) -> str:
        return ' '.join(i.capitalize() for i in name.strip().split())
    def ethicBonus(self, ethnic):
        return 0 if ethnic == 'Kinh' else 1.5
    def areaBonus(self, area):
        if area == '1': return 1.5
        if area == '2': return 1
        return 0
    def __str__(self) -> str:
        return '{:s} {:s} {:.1f} {:s}'.format(self.id, self.name, self.score, self.status)

list = []
for i in range(int(input())):
    list.append(Candidate(i+1, input(), float(input()), input(), input()))
print(*sorted(list, key=lambda e: (-e.score, e.id)), sep='\n')