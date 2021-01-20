def deflt(n,v1='Good Morning'):
    b=1
    l=[]
    for _ in range(n):
        a=input(f'Enter name {b} : ')
        l.append(a)
        b+=1
    for i in l:
        print(v1,i)    
n1=int(input('how many members are there..?\n : '))
deflt(n1)
