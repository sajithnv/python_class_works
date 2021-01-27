#question is a leter presending or not
a='programming is your carrier'
i=str(input('Enter a letter: '))
if a.count(i)==0:
    print(f'letter {i} not in this string')
else:
    print(f'leter {i} in presented {a.count(i)} times')

#this prgrm for how many times 
'''
a=input('Enter a string or num or combination: ')
##n=str(input('Enter a letter: '))
l=[]
for i in a:
    if i in l:
        continue   
    elif a.count(i)==0:
        print(f'letter {i} not in this string')
    else:
        print(f'leter {i} in presented {a.count(i)} times')
    l.append(i)    
print(l)
'''
