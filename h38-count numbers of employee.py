class employee:
    def count(s,n):
        l=[]
        for i in range(n):
            a=input('enter name: ')
            l.append(a)
        print(l)
        a2=len(l)
        print("total employees: ",a2)
r=int(input('enter the range: '))        
obj=employee()
obj.count(r)
