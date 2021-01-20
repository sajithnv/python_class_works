def fib(n):
    a=0
    b=1
    c=0
    print(a,',',b,end='')
    for i in range(1,n+1):
        c=a+b
        a=b
        b=c
        if c>n:
            return '\n prgm completed'
        print(',',c,end='')
n1=int(input("Enter a num: "))
fib(n1)        
