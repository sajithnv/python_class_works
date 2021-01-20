while True:
    a=int(input('Enter three ages: '))
    b=int(input(': '))
    c=int(input(': '))
    print('a=',a,' b=',b,' c=',c)
    if a<b and a<c:
        print('a is young',a)
    elif b<a and b<c:
        print('b is young',b)
    elif c<a and c<b:
        print('c is young',c)
    elif a>b and b==c:
        print('b and c are same ..and young ')
    elif b>a and a==c:
        print('a and c are same ..and young ')
    elif c>a and b==a:
        print('b and a are same ..and young ')    
    else:
        print('all ages are same!!')

        
