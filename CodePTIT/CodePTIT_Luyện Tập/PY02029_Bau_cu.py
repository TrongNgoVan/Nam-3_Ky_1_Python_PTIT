n, k = [int(i) for i in input().split()]
d = {}

def rankSecond(max):
    for k, v in d.items():
        if v < max:
            print(k)
            return
    print('NONE')

for i in input().split():
    d.update({i : 1 if not i in d.keys() else d.get(i) + 1})
d = dict(sorted(d.items(), key=lambda e: (-e[1], e[0])))
max = list(d.values())[0]
rankSecond(max)
        

