for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    st = []
    for i in range(0, n):
        while len(st) and a[st[-1]] <= a[i]: st.pop()
        if not len(st): print(i+1, end=' ')
        else:   print(i - st[-1], end=' ')
        st.append(i)
    print()