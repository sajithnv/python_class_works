#eg for __positional arguments__

def add(a,b):
    print(a,b)
    return a+b
c=add(10,20)
print(c)    

#here 10 for 'a' and 20 for 'b'
print('________________________')

#eg for __keyword arguments__

def add(a,b):
    print(a,b)
    return a+b
c=add(b=10,a=20)
print(c) 

#here 10 for 'b' and 20 for 'a'
print('________________________')

#eg for __default arguments___
def add(a,b=20):#default value 20 if am not giving any value for b it ...
    print(a,b)  #consider default else it overright the default value
    return a+b
c=add(10)
print(c)
print('________________________')

#eg for __variable length argument__
def add(*v):
    return v
print(add(10,20,40,'sdfgh'))
