list1 = set(' '.join(open('DATA1.in', 'r')).strip().lower().split())
list2 = set(' '.join(open('DATA2.in', 'r')).strip().lower().split())
print(*sorted(list1-list2))
print(*sorted(list2-list1))
