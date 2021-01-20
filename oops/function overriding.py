#function overriding
#same function name
#only access the child class
class parent:
    def fun(s):
        print('parent class')
class child(parent):
    def fun(s):
        print('child class')
c=child()
c.fun()
