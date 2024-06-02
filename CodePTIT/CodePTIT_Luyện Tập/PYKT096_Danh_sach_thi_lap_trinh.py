class Team:
    def __init__(self, id, name, uni) -> None:
        self.id = 'Team{:02d}'.format(id)
        self.name = name
        self.uni = uni
    
class Candidate:
    def __init__(self, id, name, team) -> None:
        self.id = 'C{:03d}'.format(id)
        self.name = name
        self.team = team
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.team.name} {self.team.uni}'

teams = [Team(i+1, input(), input()) for i in range(int(input()))]
candidates = []
for i in range(int(input())):
    name, team = input(), input()
    for j in teams:
        if j.id == team:
            candidates.append(Candidate(i+1, name, j))
            break
print(*sorted(candidates, key=lambda e: e.name), sep='\n')