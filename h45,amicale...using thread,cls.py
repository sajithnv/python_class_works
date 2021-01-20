import threading
class ami(threading.Thread):
    def run(s):
        n1=int(input('Enter two numbers: '))
        n2=int(input(': '))
        num1=n1
        num2=n2
        s1=0
        s2=0
        for i in range(1,n1):
            if n1%i==0:
                s1+=i
        for j in range(1,n2):
            if n2%j==0:
                s2+=j
        print(num1,num2)
        print(s2,s1)
        if num1==s2 and num2==s1:
            print('amicable')
        else:
            print('not')
t1=ami()
t1.start()
