d={1:'apple',2:'mango',3:'grape'}
print(d)
d.update({4:'banana'})
print(d)
d[2]='ango'
print(d)
d.pop(2)
print(d)
print(d.keys())
print(d.values())
print(d.items())
print(d[3])
a=d.clear()
print(a)
print('________________________')
d2=dict(name='abc',age=48)
print(d2)
d2.update(clas=10)
print(d2)
d2['name']='bcd'
print(d2)
d2.pop('name')
print(d2)
print(d2.keys())
print(d2.values())
print(d2.items())
print(d2['age'])
a1=d2.clear()
print(a1)
