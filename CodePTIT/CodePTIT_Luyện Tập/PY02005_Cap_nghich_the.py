def count(a):
    k = 0
    for i in range(len(a)):
        for j in range(i):
            if a[j] > a[i]: k += 1
    return k
def separate ():
    a = list(map(int, input().split()))
    print(count(a))
n = input()
separate()