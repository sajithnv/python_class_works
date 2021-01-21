##l=[10,50,40,10,60,10]
##n=10
##for i in l:
##    if i==n:
##        l.remove(i)
##print(l)        
p=[]
print(f'list P :{p}')
n=int(input('How many elements u want to add in list \'p\' :'))
i=1
for _ in range(n):
    p.append(int(input(f'enter element {i} : ')))
    i+=1
print(f'Current list p :{p}')
while True:
    print('_____________________________________________________________________')
    print('___Available opertions___\n')
    a=int(input('1.Add an element\n2.Delete an element\n3.Clear the list\n4.Add a list inside the current list\n5.Exit\nOption: '))
    if a<=0 and a>=5:
        print('___Choose a currect option___ ')
        print(f'list p :{p}')    
    elif a==1:    
        m=int(input('Which element u want to add...??\n    : '))
##        for i in p :
##            if i==m:
        if m in p:
            print('__hv the same value__')
            z=input('Do you want to continue..?y or n: ')
            if z=='y':
                p.append(m)
                print(f'___ {m} added Successfuly___')
                print(f'Current list p :{p}')
            elif z=='n':
                print(f'___Adding {m} rejected Successfuly__')
                print(f'Current list p :{p}')
            else:
                print('u r crazy...EXIT')
                break
        else:
            p.append(m)
            print(f'___ {m} added Successfuly___')
            print(f'Current list p :{p}')
        
    elif a==2:
        m=int(input('Which element u want to delet...??\n    : '))
##        for i in p :
##            if i==m:
        if m in p:
            print(f'there is {m}')
            z=input('r u sure.?y or n: ')
            if z=='y':
                p.remove(m)
                print(f'___ {m} Removed Successfuly___')
                print(f'Current list p :{p}')
            elif z=='n':
                print(f'___Removing {m} rejected Successfuly___')
                print(f'Current list p :{p}')
            else:
                print('u r crazy...EXIT')
        else:        
            print(f'there is no {m}')
            print(f'Current list p :{p}')
            print('___Try an element in the list___')      
    elif a==3:
        z=input('are you sure..?y or n :')
        if z=='y':
            p.clear()
            print('___Clear the list Successfuly___')
            print(f'Current list p :{p}')
        elif z=='n':
            print('___(clearing the list)Task Rejected Successfuly___')
            print(f'Current list p :{p}')
        else:
            print('u r crazy...EXIT')
            break
    elif a==5:
        z=input('are you sure..?y or n :')
        if z=='y':
            print('****program compleated Successfuly****')
            print('Exit')
            break      
        elif z=='n':
            print('___Task rejected Successfuly___')
        else:
            print('u r crazy...EXIT')
            break
    elif a==4:
        def a(*v):
            for i in v:
                p.append(i)
        m=int(input('how many elements: '))
        v=[]
        x=1
        for i in range(m):
            y=int(input(f'num {x}: '))
            v.append(y)
            x+=1    
        a(v)
        print('___Added a new list inside the current list Successfuly___')
        print(f'Current list p :{p}')
        

    
