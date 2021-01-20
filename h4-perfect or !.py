#perfect or not
n=int(input('Enter a number: '))
s=0
for i in range(n-1,0,-1):
    if n%i==0:
        s+=i
if s==n:
    print('Entered num is perfect....')
else:
    print("not a prfct num!!!@@@")
        
