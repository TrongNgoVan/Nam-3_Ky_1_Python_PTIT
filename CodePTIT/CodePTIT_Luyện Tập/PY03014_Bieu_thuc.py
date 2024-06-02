for __ in range(int(input())):
    s, list, count = input(), [], 0
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
            list += [count]
            print(count, end=' ')
        elif s[i] == ')':
            print(list[-1], end=' ')
            list.pop()
    print()