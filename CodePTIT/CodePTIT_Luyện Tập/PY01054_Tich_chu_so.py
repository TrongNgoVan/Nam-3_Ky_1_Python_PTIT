def multiply (n):
    res = 1
    for i in n:
        i = int(i)
        if i:
            res *= i
    return res

for t in range(int(input())):
    n = input()
    print(multiply(n))