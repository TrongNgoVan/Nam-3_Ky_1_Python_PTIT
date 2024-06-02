def isValid (a, val):
    for i in a:
        if i != val:  return False
    return True

def absolute (a):
    b = []
    for i in range(3):
        b.append(abs(a[i]-a[i+1]))
    b.append(abs(a[3]-a[0]))
    return b
def solution (a):
    cou = 0
    while isValid(a, a[0]) == False:
        a = absolute(a)
        cou += 1
    print(cou)

while True:
    a = list(map(int, input().split()))
    if isValid(a, 0):  break
    else:
        solution(a)
