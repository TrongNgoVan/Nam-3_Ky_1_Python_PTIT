def findIndex(n, k):
    tmp = 1 << n-1 ;
    if k == tmp:    return (chr)(ord('A') + n-1)
    if k > tmp:     k -= tmp
    return findIndex(n-1, k)


for t in range(int(input())):
    n, k = [int(i) for i in input().split()]
    print(findIndex(n, k))