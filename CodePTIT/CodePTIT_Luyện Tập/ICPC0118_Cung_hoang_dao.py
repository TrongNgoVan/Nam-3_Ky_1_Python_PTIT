def correctZodiac(a):
    if (int(a[1])==3 and int(a[0])>=21) or (int(a[1])==4 and int(a[0])<=19):
        return 'Bach Duong'
    if (int(a[1])==4 and int(a[0])>=20) or (int(a[1])==5 and int(a[0])<=20):
        return 'Kim Nguu'
    if (int(a[1])==5 and int(a[0])>=21) or (int(a[1])==6 and int(a[0])<=20):
        return 'Song Tu'
    if (int(a[1])==6 and int(a[0])>=21) or (int(a[1])==7 and int(a[0])<=22):
        return 'Cu Giai'
    if (int(a[1])==7 and int(a[0])>=23) or (int(a[1])==8 and int(a[0])<=22):
        return 'Su Tu'
    if (int(a[1])==8 and int(a[0])>=23) or (int(a[1])==9 and int(a[0])<=22):
        return 'Xu Nu'
    if (int(a[1])==9 and int(a[0])>=23) or (int(a[1])==10 and int(a[0])<=22):
        return 'Thien Binh'
    if (int(a[1])==10 and int(a[0])>=23) or (int(a[1])==11 and int(a[0])<=22):
        return 'Thien Yet'
    if (int(a[1])==11 and int(a[0])>=23) or (int(a[1])==12 and int(a[0])<=21):
        return 'Nhan Ma'
    if (int(a[1])==12 and int(a[0])>=22) or (int(a[1])==1 and int(a[0])<=19):
        return 'Ma Ket'
    if (int(a[1])==1 and int(a[0])>=20) or (int(a[1])==2 and int(a[0])<=18):
        return 'Bao Binh'
    if (int(a[1])==2 and int(a[0])>=19) or (int(a[1])==3 and int(a[0])<=20):
        return 'Song Ngu'

for t in range(int(input())):
    print(correctZodiac([int(i) for i in input().split()]))