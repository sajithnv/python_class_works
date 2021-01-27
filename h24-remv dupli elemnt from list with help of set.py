l=[]
l1=[]
n=int(input('how many elmnt in ur new list?? : '))
num=1
for i in range(n):
    l.append(int(input(f'num {num} : ')))
    num+=1
s=set()    
for j in l:
    s.add(j)
for k in s:
    l1.append(k)
print(f'List l: {l}\nSet s: {s}\nNew List l1: {l1}')
