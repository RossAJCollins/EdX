s = str(input('String: '))
count = 0
for x in s:
    if x == 'a':
        count = count +1
    elif x == 'e':
        count = count +1
    elif x == 'i':
        count = count +1
    elif x =='o':
        count = count +1
    elif x =='u':
        count = count +1
count = str(count)  
print('Number of vowels: '+count)    