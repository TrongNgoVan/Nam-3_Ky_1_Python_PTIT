line = open('CONTACT.in', 'r')
list = {i.lower().strip() for i in line}
print(*sorted(list, key=lambda e: e), sep='\n')