#filter()
#finding odd and even num
p=[10,20,33,34,2,7,9,12]
'''a=int(input(": "))
   p.extend([a])'''
print('given list: ',p)
a=list(filter(lambda e:e%2==1,p))
b=list(filter(lambda a:a%2==0,p))
print('even number in the given list: ',b)
print('odd number in the given list: ',a)
