#class variable
class myclass:
    a=10
m=myclass()
m1=myclass()
print(m.a)
print(m1.a)
print('_________________________')
#instance variable
class myclass:
    def display(self,a):   #self is used for access the data outside the class
        print(a)           #known as ''encapsulation''
m=myclass()
m1=myclass()
m.display(10)
m1.display(5)
