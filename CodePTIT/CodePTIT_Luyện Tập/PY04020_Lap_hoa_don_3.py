class Bill:
    def __init__(self, id, name, amount, price, discount) -> None:
        self.id = id
        self.name = name
        self.amount = amount
        self.price = price
        self.discount = discount
        self.total = price * amount - discount
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.amount} {self.price} {self.discount} {self.total}'

list = []
for __ in range(int(input())):
    list.append(Bill(input(), input(), int(input()), int(input()), int(input())))
print(*sorted(list, key=lambda e: -e.total), sep='\n')