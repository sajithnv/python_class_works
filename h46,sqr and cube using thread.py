import threading 
def sqr(a):
    c=a**2
    print(c)
def cube(a):
    c=a**3
    print('\n',c)
x=int(input('Enter two num: '))
y=int(input(': '))
t1=threading.Thread(target=sqr,args=(x,))
t2=threading.Thread(target=cube,args=(y,))
t1.start()
t2.start()

