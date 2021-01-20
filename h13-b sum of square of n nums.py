def square(n):
    if n==1:
        return 1
    else:
        return n**2+square(n-1)
n1=int(input('Enter a Range : '))
print(square(n1))
