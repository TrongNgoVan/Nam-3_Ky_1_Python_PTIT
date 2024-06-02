from datetime import datetime


class CaThi:
    def __init__(self, id, ngay, gio, phong) -> None:
        self.id = 'C{:03d}'.format(id)
        self.ngay = ngay 
        self.gio = gio
        self.phong = phong
    def __str__(self) -> str:
        return f'{self.id} {self.ngay} {self.gio} {self.phong}'

f = open('CATHI.in', 'r')
list = [CaThi(i+1, next(f).strip(), next(f).strip(), next(f).strip()) for i in range(int(next(f).strip()))]
print(*sorted(list, key=lambda e: (datetime.strptime(e.ngay + ' ' + e.gio, '%d/%m/%Y %H:%M'), e.id)), sep='\n')