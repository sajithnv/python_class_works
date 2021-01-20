#hybrid inheritance
##multi_level and single inheritance
class a:
    def fun1(s):
        print('cls a')
class b(a):
    def fun2(s):
        print('cls b')
class c(a):
    def fun3(s):
        print('cls c')
class d(b):
    def fun4(s):
        print('cls d')
class e(c):
    def fun5(s):
        print('cls e')
d=d()
e=e()
d.fun1()
d.fun2()
e.fun3()
d.fun4()
e.fun5()
