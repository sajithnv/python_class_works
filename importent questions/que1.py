class comp:
    def __init__(x):
        x.__maxprice=900
    def sell(x):
        print('selling price is: ',x.__maxprice)
    def getmaxprice(x,price):
        x.__maxprice=price
c=comp()
c.sell()
c.__maxprice=1000
c.sell()
c.getmaxprice(1000)
c.sell()
