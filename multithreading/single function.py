import threading
def fun1(a,b):
    for i in range(a,b+1):
        print(i)
##t1=threading.Thread(target=fun1,args=(1,5,))
##t2=threading.Thread(target=fun1,args=(6,10,))
##t1.start()
##t2.start()
a=int(input(': '))
b=int(input(': '))
t1=threading.Thread(target=fun1,args=(a,b,))
print('__________________')
a=int(input(': '))
b=int(input(': '))
t2=threading.Thread(target=fun1,args=(a,b,))
print('__________________')
a=int(input(': '))
b=int(input(': '))
t3=threading.Thread(target=fun1,args=(a,b,))
print('_________OUTPUT_________')
t1.start()
t2.start()
t3.start()

