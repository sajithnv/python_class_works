# Multi_level Inheritance
class a:
    def fun1(s):
        print( 'cls a')
class b(a):
    def fun2(s):
        print('cls b')
class c(b):
    def fun3(s):
        print('cls c')
class d(c):
    def fun4(s):
        print('cls d')
class e(d):
    def fun5(s):
        print('cls e')        
obj=e()
obj.fun1()
obj.fun2()
obj.fun3()
obj.fun4()
obj.fun5()

        
