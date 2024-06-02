P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
def Encode(k, s):
    for i in range(len(s)):
        pos = (ord(s[i]) - ord(P[0]) + k) % 28
        pos = (P.find(s[i]) + k) % 28
        s = s[:i] + P[pos] + s[i+1:]
    s = s[::-1]
    print(s)
while True:
    Input = input()
    if Input == '0':  break
    else:
        k, s = Input.split()
        k = int(k)
        Encode(k, s)


