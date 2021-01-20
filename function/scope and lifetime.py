# scope and lifetym of a variable
b=100
def fun():
    global b
    b=30
    return b
def fun1():
    return b
print(b)
print(fun())
print(fun1())
print(b)
