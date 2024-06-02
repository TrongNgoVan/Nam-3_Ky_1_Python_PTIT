n = int(input())
list = []
for i in [int(j) for j in input().split(' ')]:
    if len(list) and (not (list[len(list) - 1] + i) % 2):
        list.pop()
    else:
        list.append(i)
print(len(list))