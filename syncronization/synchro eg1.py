import threading
x=0
def inc():
    global x
    x+=1
def sub_task(y):
    for _ in range(100000):
        y.acquire()
        inc()
        y.release()
def main_task():
    global x
    x=0
    l=threading.Lock()
    t1=threading.Thread(target=sub_task,args=(l,))
    t2=threading.Thread(target=sub_task,args=(l,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
if __name__ =='__main__':
    for i in range(1,11):
        main_task()
        print('iteration',i,'-',x)
