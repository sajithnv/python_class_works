##class c1:
##    def f1(s,h):
##        print('cat',x)
##class c2(c1):
##    def f2(s):
##        print('cat has 4 legs')
##class c3(c2):
##    def f3(s,h):
##        print('cat',y)
##class c4(c3):
##    def f4(s):
##        print('cat can\'t fly')
##class c5(c4):
##    def f5(s,h):
##        print('cat',z)        
##class c6(c5):
##    def f6(s,h):
##        print('bat',x)
##class c7(c6):
##    def f7(s,h):
##        print('bat',y)
##class c8(c7):
##    def f8(s,h):
##        print('bat',z)
##x='is an animal'
##y='can\'t swim'
##z='is a warm blooded animal'
##o=c8()
##o.f1(x)
##o.f2()
##o.f3(x)
##o.f4()
##o.f5(x)
##o.f6(x)
##o.f7(x)
##o.f8(x)
'''end'''
class c1:
    def __init__(s,a,x):
        print(a,x)
        print(a,' has 4 legs')
        print(a,y)
        print(a,'can\'t fly')
        print(a,z)
class c2:
    def __init__(s,b,x):
        print(b,x)
        print(b,y)
        print(b,z)
a='cat'
b='bat'
x='is an animal'
y='can\'t swim'
z='is a warm blooded animal'
c=c1(a,x)
d=c2(b,x)



                

