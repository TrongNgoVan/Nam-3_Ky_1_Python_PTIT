class Result:
    def getScore(self,n):
        if n >= 39: return 9
        if n >= 37: return 8.5
        if n >= 35: return 8
        if n >= 33: return 7.5
        if n >= 30: return 7
        if n >= 27: return 6.5
        if n >= 23: return 6
        if n >= 20: return 5.5
        if n >= 16: return 5
        if n >= 13: return 4.5
        if n >= 10: return 4
        if n >= 7: return 3.5
        if n >= 5: return 3
        if n >= 3: return 2.5
        return 0
    def rounded(self,n):
        decimal = n - int(n)
        if decimal >= 0.75: return int(n) + 1
        if decimal >= 0.25: return int(n) + 0.5
        return int(n)
    def __init__(self, score) -> None:
        self.score = (self.getScore(score[0]) + self.getScore(score[1]) + score[2] + score[3]) / 4
        pass
    def __str__(self) -> str:
        return '{:.1f}'.format(self.rounded(self.score))
        
for t in range(int(input())):
    print(Result([float(i) for i in input().split()]))
# 2
# 15 25 5.0 5.5
# 22 32 6.0 6.0