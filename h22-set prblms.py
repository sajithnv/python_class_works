a=set()
b=set()
a1=int(input('how many elements in set A: '))
num=1
for i in range(a1):
    a.add(int(input(f'Num {num}: ')))
    num+=1
b1=int(input('how many elements in set b: '))
num=1
for i in range(b1):
    b.add(int(input(f'Num {num}: ')))
    num+=1        
#find identical elements
print('identical elements')
print('_________________________')
print(a&b)
print(a.intersection(b))
#form a new list avoid duplicate elements
print('a new list avoid duplicate elements')
print('_________________________')
print(a|b)
print(a.union(b))
