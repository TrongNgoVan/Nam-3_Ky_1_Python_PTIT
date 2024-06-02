n, m = [int(i) for i in input().split()]
a = {int(i) for i in input().split()}
b = {int(i) for i in input().split()}
print(*sorted(a&b, key=lambda e: e))
print(*sorted(a^(a&b), key=lambda e: e))
print(*sorted(b^(a&b), key=lambda e: e))