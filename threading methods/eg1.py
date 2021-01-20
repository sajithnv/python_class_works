import threading
def display():
    print(threading.activeCount())
    print(threading.currentThread())
    print(threading.enumerate())
t=threading.Thread(target=display)
t.start()
