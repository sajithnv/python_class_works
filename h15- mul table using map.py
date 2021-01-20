l=[]
for i in range(1,11):
    l.append(i)
n=int(input('Which mul tble u want : '))
x=1
for j in map(lambda a:a*n,l):
    print(f'{x}*{n}= {j}')
    x+=1
