def add(n):
    return lambda n1:n+n1
a=int(input('enter the first num: '))
b=int(input('enter the second num: '))
x=add(a)
print(x(b))
