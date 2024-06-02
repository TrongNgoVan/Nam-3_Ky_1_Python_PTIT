class Complex:
    def __init__(self, real = None, imaginary = None):
        self.real = int(real)
        self.imaginary = int(imaginary)
        
    def __add__(self, other):
        return Complex(self.real+other.real, self.imaginary+other.imaginary)
    
    def __mul__(self, other):
        return Complex(self.real*other.real-self.imaginary*other.imaginary, self.real*other.imaginary+self.imaginary*other.real)
    
    def __str__(self):
        return str(self.real) + (' + ' + str(self.imaginary) if self.imaginary >= 0 else ' - ' + str(abs(self.imaginary))) + 'i'
    
for t in range(int(input())):
    a1, a2, b1, b2 = [int(i) for i in input().split()]
    A = Complex(a1, a2)
    B = Complex(b1, b2)
    s = A + B
    C = s * A
    D = s * s
    print(C, D, sep=', ')
    