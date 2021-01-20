n=int(input('Enter a 3 digit num: '))
s=0
while n!=0:
    print(f'n={n},s={s}')
    m=n%10
    s+=m**3
    n=n//10
    print(f'n={n},m={m},s={s}')
    print('_____________________')
print(s)    
    
