# Single Inheritance
class a:
    def fun1(s1):
        print('class a')
class b(a):
    def fun2(s2):
        print('class b')
obj=b()
obj.fun1()
obj.fun2()
