#decorator
def fun1(a,b):
    return a+b
x=str(input(':'))
y=str(input(':'))
print(fun1(x,y))
fun2=fun1
x=str(input(':'))
y=str(input(':'))
print(fun2(x,y))
