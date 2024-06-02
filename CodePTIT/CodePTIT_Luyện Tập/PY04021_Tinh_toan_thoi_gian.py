from datetime import datetime 

class Player:
    def __init__(self, id, name, start, end) -> None:
        self.id = id
        self.name = name
        self.difference = (datetime.strptime(end, '%H:%M') - datetime.strptime(start, '%H:%M')).seconds
    def __str__(self) -> str:
        return '{} {} {} gio {} phut'.format(self.id, self.name, self.difference//3600, self.difference%3600//60)

player = [Player(input(), input(), input(), input()) for i in range(int(input()))]
player.sort(key=lambda e: -e.difference)

print(*player, sep='\n')
# 3
# 01T
# Nguyen Van An
# 09:00
# 10:30
# 06T
# Hoang Van Nam
# 15:30
# 18:00
# 02I
# Tran Hoa Binh
# 09:05
# 10:00
