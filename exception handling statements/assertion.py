#AssertionError:
def temp(t):
    assert(t>0),"Can't be Zero"
    return t-273
print(temp(100))
print(temp(-100))
