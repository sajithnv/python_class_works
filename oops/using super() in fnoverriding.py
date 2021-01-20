#super()
#fncn overriding
class parent:
    def fun(s):
        print('parent class')
class child(parent):
    def fun(s):
        print('child class')
        super().fun()
c=child()
c.fun()
