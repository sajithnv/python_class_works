a=(6,12,18,24,30,36,42)
n=int(input('How many elements : '))
n2=1
b=[]
c=[]
for _ in range(n):
    n1=int(input(f'num {n2}: '))
    if n1 in a:
        b.append(n1)
    else:
        c.append(n1)
    n2+=1
print(a)    
print('The new list(elemnts in this list should be there in tuple a)\n   b: ',tuple(b))
print('The new list (elements in this list not there in tuple a)\n    c: ',tuple(c))
print('_____Comparing_____\n')
print(a)
for i in b:
    x=i in a
    print(f'{i} in tuple a = ',x)
for i in c:
    y=i not in a
    print(f'{i} not in tuple a = ',y)
if x and y:
    print('***Project Completed Successfuly****')
else:
    print('something wen\'t wrong !!!')
