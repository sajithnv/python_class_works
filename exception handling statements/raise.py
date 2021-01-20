#raise
while True:
    try:
        a=int(input("Enter two nums: "))
        b=int(input(": "))
        if b==0:
            raise ZeroDivisionError('cant div by 0')
        c=a/b
        print(c)
    except ZeroDivisionError as e:
        print(e)
    except BaseException:
        print('an error')
    finally:
        print('prgm compltd')
