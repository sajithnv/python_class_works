#way 1
'''
def wish(a):
    while True:
        print('\n______start_________________________________')
        print('___Choose a wish___')
        w=int(input('1.Good Morning\n2.Good Afternoon\n3.Good Evening\n4.Good Night\n5.Happy Birthday\n6.Exit\nSelect a number: '))
        print('_________________OutPut____________________\n')
        if w==0 and w>6:
            print('wrong input!!!!')
            break
        elif w==1:
            print(f'Good Morning {a}')
        elif w==2:
            print(f'Good Afternoon {a}')
        elif w==3:
            print(f'Good Evening {a}')
        elif w==4:
            print(f'Good Night {a}')
        elif w==5:
            print(f'Happy Birthday \'{a}\'')
        elif w==6:
            print('prgm complt sucsfly')
            break      
a=input('Enter a name to wish: ')
wish(a)
'''    
#way 2
from datetime import *
import time

now=datetime.now()
print(now)
h=int(now.strftime('%H'))
b=now.strftime('%m,%d')
def wish(a,h,b):
    print('_________________OutPut____________________\n')
    if h>=0 and h<12:
        print(f'Good Morning {a}')
    elif h>=12 and h<16:
        print(f'Good Afternoon {a}')
    elif h>=16 and h<20:
        print(f'Good Evening {a}')
    elif h>=20:
        print(f'Good Night {a}')
    if b==('12,25'):
        print(f'Happy Birthday and HAppy christmas\'{a,now}\'')
    if b==('12,26'):
        print(f'Happy Republic day {a,now}')
    if b==('01,01'):
        print(f'Happy NewYear {a,now}')
    if b==('02,20'):
        print(f'Happy Birthday {a,now}')     
a=input('Enter a name to wish: ')
wish(a,h,b)
