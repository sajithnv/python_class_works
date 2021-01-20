#super
class bird:
    def __init__(s):
        print('bird is ready')
    def whoisthis(s):
        print('bird')
    def swim(s):
        print('swim fast')
class penguine(bird):
    def __init__(s):
        super().__init__()
        print('penguine is ready')
    def whoisthis(s):
        super().whoisthis()
        print('penguine')
    def run(s):
        print('penguine run fast')
p=penguine()
p.whoisthis()
p.swim()
