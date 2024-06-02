s = input()

def isUp ():
    up, low = 0, 0
    for i in s:
        if i>='A' and i <='Z':  up += 1
        elif i>='a' and i <='z': low += 1
    return True if up > low else False

print (s.upper() if isUp() else s.lower())
