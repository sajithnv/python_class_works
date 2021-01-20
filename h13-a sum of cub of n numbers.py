def cube(n):
    if n==1:
        return 1
    else:
        return n**3+cube(n-1)
n1=int(input('Enter a Range : '))
print(cube(n1))
