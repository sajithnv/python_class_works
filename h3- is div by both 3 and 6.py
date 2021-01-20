while True:
    n=int(input('Enter a number: '))
    if n==0:
        print("Enter a num greater than zero")
        continue
    if n%3==0:
        if n%6==0:
            print('div by both 3 and 6')
        else:
            print('div by 3 only')
    else:
        print('cant div by both 3 and 6')
            
