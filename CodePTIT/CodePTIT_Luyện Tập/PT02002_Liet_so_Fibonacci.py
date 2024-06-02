fibo = [0, 1, 1]
for i in range(3, 93):
    fibo.append(fibo[i-1] + fibo[i-2])
for t in range(int(input())):
    a, b = [int(i) for i in input().split()]
    print(*fibo[a:b+1])