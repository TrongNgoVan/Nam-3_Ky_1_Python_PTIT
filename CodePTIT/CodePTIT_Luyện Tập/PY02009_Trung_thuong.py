from collections import Counter


for t in range(int(input())):
    a = Counter(sorted(int(input()) for i in range(int(input()))))
    
    print(a.most_common(1)[0][0])
    # most_common return an array list
    # add [0] to get first element of list 