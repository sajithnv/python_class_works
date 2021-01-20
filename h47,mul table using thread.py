import threading
def mul(n):
    x=1
    for i in range(n,(n*10)+1,n):
        print(x,'*',n,'=',i)
        x+=1
n=int(input(':'))                
t=threading.Thread(target=mul,args=(n,))
t.start()
