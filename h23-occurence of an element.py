#1
a=[4,6,2,7,6,9,1,5,8,8,3,4]
n=int(input('Enter the num u want to know the count: '))
s=a.count(n)
print(f'list A: {a}\n{n} num repeated {s} times...')        
print('_____________________________________________')
#2
print(f'list A: {a}\n')
l=[]
for i in a:
    if i in l:
        continue
    else:
        l.append(i)
        s1=a.count(i)
        print(f'{i} num repeated {s1} times...')        
