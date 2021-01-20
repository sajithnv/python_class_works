#eg1
'''
def geno():
    for i in range(1,10+1):
        yield i*i
for x in geno():
    print(x)
'''
#eg2
def gene(a):
    n=0
    for i in range(a+1):
        n+=i
        yield n
for x in gene(int(input('RANGE???'))):
    print(x)
##print(gene(int(input('RANGE???'))))

#eg3
'''
def a():
    for i in range(5,51,5):
        yield i
b=1
for s in a():
    print('5*',b,'=',s)
    b+=1
'''

        
