from math import sqrt


p = [1 for i in range(int(1e5))]
p[0] = p[1] = 0
for i in range(2, int(sqrt(1e5)) + 1):
    if p[i]:
        for j in range(i*2, int(1e5), i):
            p[j] = 0

for t in range(int(input())):
    print("YES" if p[int(input()[-4::])] else "NO")