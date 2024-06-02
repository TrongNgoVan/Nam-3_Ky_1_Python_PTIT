list = [len(input().split()) for i in range(int(input()))]
res = []
i = 0
while i < len(list):
    if list[i] == 7:
        i += 4
        res += [2]
    elif list[i] == 6:
        i += 2
        res += [1]
        while i < len(list) and list[i] == 6:
            i += 2
print(len(res), *res, sep='\n')
# 8
# Minh ve minh co nho ta
# Muoi lam nam ay thiet tha man nong
# Minh ve minh co nho khong
# Nhin cay nho nui nhin song nho nguon
# Mot canh hai canh lai ba canh
# Tran troc ban khoan giac chang lanh
# Canh bon canh nam vua chop mat
# Sao vang nam canh mong hon bay