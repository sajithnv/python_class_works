class complex:
    def __init__(s,x1,y1):
        s.x1=x1
        s.y1=y1
    def __add__(s,h):
        real=s.x1+h.x1
        img=s.y1+h.y1
        return complex(real,img)
    def __str__(s):
        return str(s.x1)+'+'+str(s.y1)
c1=complex(3,2)
c2=complex(5,4)
print('the given values are :\n(x1,y1) :',c1,'\n (x2,y2) :',c2)
print('Result of (x1+x2)+(y1+y2) = ',c1+c2)

