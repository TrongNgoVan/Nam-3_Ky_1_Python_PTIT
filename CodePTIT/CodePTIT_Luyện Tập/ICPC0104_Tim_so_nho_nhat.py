import re


for t in range(int(input())):
    n = [int(i) for i in re.findall("\\d+", input())]
    print(min(n))