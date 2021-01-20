#else and finally
try:
    a=int(input("Enter two nums: "))
    b=int(input(": "))
    c=a/b
except ZeroDivisionError:
    print('cant divide by 0')
except BaseException:
    print('an error')
else:
    print('Result is: ',c)
finally:
    print('program compleated')
