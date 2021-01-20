#hibrid Inheritance
class a:
    def fun1(s):
        print('cls a')
class b(a):
    def fun2(s):
        print('cls b')
class c(a):
    def fun3(s):
        print('cls c')
class d(b,c):
    def fun4(s):
        print('cls d')        
obj=d()
obj.fun1()
obj.fun2()
obj.fun3()
obj.fun4()
