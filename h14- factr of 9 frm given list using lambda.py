##l=[3,2,4,1,6,7]
##print(list(filter(lambda a:9%a==0,l)))
l=[]
m=1
n=int(input('hw many num u want add in ur list...??\n : '))
for _ in range(n):
    n1=int(input(f'Enter element{m} : '))
    l.append(n1)
    m+=1
while True:
    print('____________again________________')
    print(l)
    z=int(input('fact of ..?\n : '))    
    print(list(filter(lambda a:z%a==0,l)))
