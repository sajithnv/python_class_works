##def var(*v):
##    for j in v:
##        print(j)
##        s=0
##        for i in range(1,j+1):
##            s+=i
##        print(f'sum of first {j} num is : {s}')    
##var(10,20)
def var(n,*v):
    m=1
    l=[]
    for _ in range(n):
        a=int(input(f'Enter the num{m}: '))
        l.append(a)
        m+=1
    for j in l:
        s=0
        for i in range(1,j+1):
            s+=i
        print(f'sum of first {j} num is : {s}')    
n1=int(input('how many numbers u wnt to entr..?\n: '))
var(n1)
