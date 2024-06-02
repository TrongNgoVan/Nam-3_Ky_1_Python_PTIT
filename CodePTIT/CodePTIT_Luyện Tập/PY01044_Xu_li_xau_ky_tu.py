a = {i for i in input().lower().split()}
b = {i for i in input().lower().split()}
print(*sorted(a|b))
print(*sorted(a&b))