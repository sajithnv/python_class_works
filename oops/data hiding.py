#data hiding usin   ' __  '(two underscore symbols)
class count:
    x=0
    def counter(s):
        s.x+=1
        print(s.x)
c=count()
c.counter()
print(c.x)
print('__________________________')
class count:
    __x=0
    def counter(s):
        s.__x+=1
        print(s.__x)
c=count()
c.counter()
print(c.__x)# here effecting the 'data_hiding'
            # we can't access data_member from outsude of a class 
