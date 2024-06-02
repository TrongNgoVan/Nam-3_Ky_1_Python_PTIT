class Candidate:
    def __init__(self, name, dob, sj1, sj2, sj3) -> None:
        self.name = name
        self.dob = dob
        self.total = sj1 + sj2 + sj3
    def __str__(self) -> str:
        return self.name + ' ' + self.dob + ' ' + '{:.1f}'.format(self.total)

print(Candidate(input(), input(), float(input()), float(input()), float(input())))