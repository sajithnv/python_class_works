def amstrong(n):
     num=n
     s=0
     c=0
     while n>=1:
         c=n%10
         s+=c**3
         n//=10
         print(n,s)    
     if num==s:
         print('Entered num is \'AMSTRONG\'')
     else:
         print('Entered num is \'NOT an AMSTRONG\'')

