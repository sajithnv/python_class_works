# function overloading
#str and integer
class over:
    def over1(s,t,*v):
        if t=='str':
            s=''
        if t=='int':
            s=0
        for i in v:
            s+=i
        print(s)
obj=over()
obj.over1('int',20,40,50,60,22)
obj.over1('str','good',' ','morning',' ','sajith')

