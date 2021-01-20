#multiplication table
n=int(input('Which mul_table you want: '))
a=1
for i in range(n,(n*10)+1,n):
    print(a,'*',n,'=',i)
    a+=1
