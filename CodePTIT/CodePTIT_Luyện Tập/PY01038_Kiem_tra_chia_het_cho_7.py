def test_case ():
    n = input()
    for t in range(1000):
        if (not int(n) % 7):
            print(n)
            return
        n = str(int(n) + int(n[::-1]))
    print("-1")

for t in range(int(input())):
    test_case()