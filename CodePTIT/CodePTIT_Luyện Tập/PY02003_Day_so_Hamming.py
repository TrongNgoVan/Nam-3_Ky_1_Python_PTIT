list = []
MAX = 10**18

i = 1
while i <= MAX:
    j = 1
    while j <= MAX:
        z = 1
        while z <= MAX:
            list += [i*j*z]
            z *= 5
        j *= 3
    i *= 2

list.sort()

def binarySearch(n, l, r) :
    if (l > r):
        return 'Not in sequence'
    mid = (l + r) // 2
    if (list[mid] == n) :   return mid + 1
    if (list[mid] < n) :    return binarySearch(n, mid + 1, r)
    return binarySearch(n, l, mid - 1)

for t in range(int(input())):
    print(binarySearch(int(input()), 0, len(list)))