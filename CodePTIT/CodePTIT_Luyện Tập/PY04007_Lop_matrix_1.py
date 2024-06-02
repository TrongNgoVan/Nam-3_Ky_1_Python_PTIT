class Matrix:
    def __init__(self, n, m, mt):
        self.n = n
        self.m = m
        self.mt = mt
        
    def __mul__(self):
        res = []
        for i in range(self.n):
            res += [[0]*self.n]
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.m):
                    res[i][j] += self.mt[i][k]*self.mt[j][k]
        return Matrix(self.n, self.n, res)
    
    def __str__(self):
        for i in self.mt:
            print(*i)
        return ''

if __name__ == '__main__':    
	for case in range(int(input())):
		n, m = [int(i) for i in input().split()]
		ip = []
		for i in range(n):
			ip.append([int(j) for j in input().split()])
		mt = Matrix(n, m, ip)
		print(mt.__mul__())