#closure
def fun1(a):
    def fun2(b):
        c=a+b
        print(c)
    return fun2
a=int(input(':'))
b=int(input(':'))
x=fun1(a)
x(b)
