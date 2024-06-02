n = int(input())
list = []
s = ''
for t in range(n):
    s = input()
    list += [s]
    if s == '':
        n += 1
        print(list[0] + ':', len(list) - 2)
        list.clear()
print(list[0] + ':', len(list) - 1)

    
# 9
# Home/accommodation
# What kind of housing/accommodation do you live in?
# Who do you live with?
# How long have you lived there?
 
# Study
# Describe your education
# What is your area of specialization?
# Why did you choose to study that major?