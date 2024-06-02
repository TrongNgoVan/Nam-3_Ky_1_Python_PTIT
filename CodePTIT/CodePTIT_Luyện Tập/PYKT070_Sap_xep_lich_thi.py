from datetime import datetime


class MonThi:
    def __init__(self, id, mon, hinhThuc) -> None:
        self.id = id
        self.mon = mon
        self.hinhThuc = hinhThuc
    def __str__(self) -> str:
        return self.mon

class CaThi:
    def __init__(self, id, ngay, gio, phong) -> None:
        self.id = 'C{:03d}'.format(id)
        self.ngay = ngay 
        self.gio = gio
        self.phong = phong
    def __str__(self) -> str:
        return f'{self.ngay} {self.gio} {self.phong}'

class LichThi:
    def __init__(self, ca, mon, nhom, soLuong) -> None:
        self.ca = ca
        self.mon = mon
        self.nhom = nhom
        self.soLuong = soLuong
    def __str__(self) -> str:
        return f'{self.ca} {self.mon} {self.nhom} {self.soLuong}'
        

mt = open('MONTHI.in', 'r')
monthi = [MonThi(next(mt).strip(), next(mt).strip(), next(mt).strip()) for i in range(int(next(mt).strip()))]

ct = open('CATHI.in', 'r')
cathi = [CaThi(i+1, next(ct).strip(), next(ct).strip(), next(ct).strip()) for i in range(int(next(ct).strip()))]

lt = open('LICHTHI.in', 'r')
lichthi = []
for i in range(int(next(lt).strip())):
    caId, monId, nhom, soLuong = [i for i in next(lt).strip().split()]
    mon, ca = '', ''
    for m in monthi:
        if m.id == monId:
            mon = m
            break
    for c in cathi:
        if c.id == caId:
            ca = c
            break
    lichthi.append(LichThi(ca, mon, nhom, soLuong))

print(*sorted(lichthi, key=lambda e: (datetime.strptime(e.ca.ngay + ' ' + e.ca.gio, '%d/%m/%Y %H:%M'), e.ca.id)), sep='\n')