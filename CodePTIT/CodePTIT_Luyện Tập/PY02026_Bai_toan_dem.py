n, isExe = int(input()), True
list = []
while True:
    try:
        list += [int(i) for i in input().split()]
    except: break
for i in range(1, max(list)):
    if i not in list:
        print(i, sep=' ')
        isExe = False
if isExe and n == len(list):   print('Excellent!')