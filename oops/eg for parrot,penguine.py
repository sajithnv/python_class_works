class parrot:
    def fly(s):
        print('parrot can fly')
    def swim(s):
        print('parrot can\'t swim')
class penguine:
    def fly(s):
        print('penguine can\'t fly')
    def swim(s):
        print('penguine can swim')
def flyorswim(x):
    x.fly()
    x.swim()
pr=parrot()
pg=penguine()
flyorswim(pr)
flyorswim(pg)
