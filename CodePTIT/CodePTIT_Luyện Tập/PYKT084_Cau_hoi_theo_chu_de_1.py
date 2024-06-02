list = []
tmp = '...'
for t in range(int(input())):
    tmp = input()
    if tmp != '':
        list += [tmp]
    else:   
        print(f'{list[0]}: {len(list) - 1}')
        list.clear()
print(f'{list[0]}: {len(list) - 1}')