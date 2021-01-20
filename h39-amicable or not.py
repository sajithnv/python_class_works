# amicable:- CONSIDER 220 & 280
#          SUM OF DIVISORS OF 220 IS = 280
#          AND SUM OF DIVISORS OF 280 IS =220
class ami:
    def amic(s,num1,num2):
        #num1=int(input('enter two num: '))
        #num2=int(input(': '))
        n1=num1
        n2=num2
        s1=0
        s2=0
        for i in range(1,num1):
            if num1%i==0:
                s1+=i
        for i in range(1,num2):
            if num2%i==0:
                s2+=i
        print('entered num n1: ',n1)
        print('result of s1: ',s1)
        print('entered num n2:',n2)
        print('result of s2: ',s2)
        if n1==s2 and n2==s1:
            print('**** AMICABLE ****')
        else:
            print('!!! Not Amicable !!!')
a=int(input('enter two nums: '))
b=(int(input(': ')))
obj=ami()
obj.amic(a,b)
