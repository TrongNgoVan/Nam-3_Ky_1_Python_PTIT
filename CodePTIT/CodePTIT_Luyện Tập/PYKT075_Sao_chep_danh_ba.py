class Contact:
    def __init__(self, name, phone, date) -> None:
        self.phone = phone
        self.date = date
        self.name = name
        self.firstName = name.split()[-1]
    def __str__(self) -> str:
        return f'{self.name}: {self.phone} {self.date}'

date = ''
list = []

st = open('SOTAY.txt', 'r')
try:
    while st:
        s = next(st).strip()
        if s.startswith('Ngay'):
            date = s[5:]
        else:
            list.append(Contact(s, next(st).strip(), date))
except StopIteration:
    st.close()

list.sort(key=lambda e: (e.firstName, e.name))

dt = open('DIENTHOAI.txt', 'w')
dt.write('\n'.join([str(i) for i in list]))
dt.close()