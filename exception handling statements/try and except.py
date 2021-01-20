#try and except
try:
    p=[1,2,3]
    print(p[0])
    print(p[1])
    print(p[2])
    print(p[3])
except IndexError:
    print('no such index found!!!')
