class complex:
    def __init__(s,r,i):
        s.r=r
        s.i=i
        print(r,i)
    def __add__(s,x):
        real=s.r+x.r
        img=s.i+x.i
        return complex(real,img)
    def __str__(s):
        return str(s.r)+'+'+str(s.i)+'i'
c1=complex(3,5)
c2=complex(2,3)
print('\n\t',c1,'\n\t',c2)
print('\t_________')
print('ans is :',c1+c2)
print('_____________________________')
'''end'''
class complex:
    def __init__(s,r,i,m):
        s.r=r
        s.i=i
        s.m=m
        print(r,i,m)
    def __add__(s,x):
        real=s.r+x.r
        img=s.i+x.i
        mid=s.m+x.m
        return complex(real,img,mid)
    def __str__(s):
        return str(s.r)+'+'+str(s.i)+'+'+str(s.m)+'i'
c1=complex(1,3,5)
c2=complex(1,2,3)
print('\n\t',c1,'\n\t',c2)
print('\t_________')
print('ans is :',c1+c2)






