#iterator
try:
    p={22,52,35.4,'dagaf'}
    print(p.__str__())
    x=iter(p)
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
except StopIteration:
    print('____________________________________')
    print('ERROR>>>\nlen(x)<no of next() lines')
    print('____________________________________')
finally:
    print('pgrm complt sucsly')
          
