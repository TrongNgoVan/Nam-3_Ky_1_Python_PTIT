def isValid (s):
    return s.count('2')*2 >= len(s) + 1
    
for t in range(int(input())):
    st, dem, n = ['1', '2'], 0, int(input())
    while dem < n:
        s = st[0]
        if isValid(s):
            print(s, end=' ')
            dem += 1
        st.append(s + '0')
        st.append(s + '1')
        st.append(s + '2')
        del st[0]
    print()
