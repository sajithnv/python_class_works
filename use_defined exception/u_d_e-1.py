while True:
    class error(Exception):
        pass
    class small(error):
        pass
    class large(error):
        pass
    try:
        num=100
        n=int(input('Enter a number: '))
        if n>num:
            raise large
        elif n<num:
            raise small
        else:
            print('u r correct')
    except large:
        print('num is too lrg')
    except small:
        print('num is too small')
        
