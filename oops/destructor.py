try:
    class mycls:
        def __init__(self,a,b):
            print(a,b)
        def show(self):
            print('wlcome')
        def __del__(self):
            pass
    obj=mycls(22,222)
    obj.show()
    del obj
    obj.show()
except BaseException: #or NameError
    pass
