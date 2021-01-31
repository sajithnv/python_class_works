#using class
'''
import threading
class c1(threading.Thread):
    def run(s):
        a=6
        print(a)
class c2(threading.Thread):
    def run(s):
        a=7
        print(a)
t1=c1()
t2=c2()
t1.start()
t2.start()
   '''
#reading input
'''
import threading
def run(a):
    print(a)
x=int(input(': '))    
t1=threading.Thread(target=run,args=(x,))
t2=threading.Thread(target=run,args=(x,))
t1.start()
t2.start()
'''
#reading input from outside a class
import threading as t
class c1(t.Thread):
    def run(self,a):
        print(a)
class c2(t.Thread):
    def run(self,b):
        print(b)
a=int(input(': '))
b=int(input(': '))        
t1=c1(a)
t2=c2(b)
t1.start()
t2.start()

