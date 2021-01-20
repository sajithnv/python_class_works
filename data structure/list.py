#built in functions in __list__
l=[10,87,45,23,12]
print(l)
l.append('abcd')
print(l)
l.extend([22,23,46])
print(l)
a=l.count(23)
print(a)
l.reverse()
print(l)
l2=[]
l2=l.copy()
print(l,l2)
l.pop(2)
print(l)
l.remove(23)
print(l)
print('L2 :',l2)
l2.clear()
print('L2 :',l2)
del l2

