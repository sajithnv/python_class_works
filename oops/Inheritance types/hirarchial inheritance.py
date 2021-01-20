# Hirarchial inheritance
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
class e(b):
    def fun5(s):
        print('cls e')
class f(c):
    def fun6(s):
        print('cls f')
class g(c):
    def fun7(s):
        print('cls g')
d=d()
e=e()
f=f()
g=g()
d.fun1()
d.fun2()
f.fun3()
d.fun4()
e.fun5()
f.fun6()
g.fun7()
        
