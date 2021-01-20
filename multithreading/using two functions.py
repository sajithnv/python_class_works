import threading
def fun1():
    a=6
    print(a)
def fun2():
    a=5
    print(a)
t1=threading.Thread(target=fun1)
t2=threading.Thread(target=fun2)
t1.start()
t2.start()
