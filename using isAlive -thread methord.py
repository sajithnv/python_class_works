import threading
def show():
    print('is alive\n')
t=threading.Thread(target=show)
t.start()
print(t.is_alive())
