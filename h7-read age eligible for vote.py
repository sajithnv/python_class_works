##while True:
##    n=int(input('Enter your age: '))
##    if n==0:
##        print('you"re not borned yet..hehehe...\n Enter again... ')
##        continue
##    elif n<18:
##        print("Oops...You're not eligible for vote!!!!!")
##    else:
##        print('Eligible for vote..')
def ages():
    l1=[]
    l2=[]
    a=int(input('how many members details u have??\n : '))
    while a!=0:
        l1.append(str(input('Enter name: ')))
        while a!=0:
            l2.append(int(input("age : ")))
            a-=1
            break
    print('_______________OUTPUT________________')    
    for j in l1:
        print(j)
        for i in l2:
            if i==0:
                print("It's a new born baby...hehehe")
                print('______________???_________________')
                l2.remove(i)
                break
            elif i<18:
                print(f'Not eligible for vote,bcz age={i} !!!!')
                print('______________!!!_________________')                
                l2.remove(i)
                break
            else:
                print(f'Eligible for vote,age={i}')
                print('______________***________________')                
                l2.remove(i)
                break
ages()        
        
        
