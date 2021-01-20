import threading
def dis():
    print('aftr 5 sec')
print('wait 5 sec')
t=threading.Timer(5,dis)
t.start()
