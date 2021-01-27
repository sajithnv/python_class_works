def perfect(n):
    s=0
    num=n
    for i in range(1,n):
        if n%i==0:
            s+=i
    if num==s:
        print('Entered number is \'Perfect\'')
    else:
        print('Entered num is \'not_perfect\'')
    

