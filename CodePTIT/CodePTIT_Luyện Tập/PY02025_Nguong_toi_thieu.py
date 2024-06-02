s, k = input(), int(input())
d = {}
for i in range(0, len(s)-1, 2):
    num = int(s[i:i+2])
    d.update({num : d.get(num)+1 if num in d.keys() else 1})
res = list(filter(lambda e: e[1] >= k, sorted(d.items(), key=lambda e: e[0])))
if not len(res):
    print("NOT FOUND")
else:
    for key, value in res:
        print(key, value)