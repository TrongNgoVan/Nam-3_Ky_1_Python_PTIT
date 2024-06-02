char = {chr(i):i-65 for i in range(ord('A'), ord('Z')+1)}
num = {i-65:chr(i) for i in range(ord('A'), ord('Z')+1)}
n = len(char)

def test_case():
    s = input()
    s1 = s[:len(s)//2]
    s2 = s[len(s)//2:]

    value1 = sum([char[i] for i in s1])
    s1= [num[(char[i] + value1) % n] for i in s1]

    value2 = sum([char[i] for i in s2])
    s2 = [num[(char[i] + value2) % n] for i in s2]

    print(''.join([num[(char[s1[i]] + char[s2[i]]) % n] for i in range(len(s1))]))

for __ in range(int(input())):
    test_case()