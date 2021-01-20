##import threading
##import time
##def show(i):
##    print('thread',i,'going to sleep for 5sec')
##    time.sleep(5)
##    print('thread',i,'awake now')
##for i in range(5):
##    t=threading.Thread(target=show,args=(i,))
##    t.start()
##    print('current thread count: ',threading.activeCount())
import threading
import time
def show(i):
    print('thread',i,'going to sleep for 5sec')
    time.sleep(5)
    print('thread',i,'awake now')
for i in range(5):
    t=threading.Thread(target=show,args=(i,))
    t.start()
    print('current working thread',threading.currentThread())
