# Multiple Inheritance
class a:
    def fun1(s1):
        print('cls a')
class b:
    def fun2(s2):
        print('cls b')
class c(b,a):
    def fun3(s3):
        print('cls c')
obj=c()
obj.fun1()
obj.fun2()
obj.fun3()


