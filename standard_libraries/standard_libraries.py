## random
'''
import random
a=random.random()
print(a)
'''
##math
'''
import math
print(math.factorial(5))
'''
##os,shutil
'''
import os,shutil,math
print(os.getcwd())
print(math.factorial(5))
'''
##glob =function search\\ sys= display full path
'''
import glob,sys
print(glob.glob('*'))
print(sys.path)
'''
##staticstics mean(),meadian()
'''
import statistics as p1
p=[5,9,10,10,15]
print(p1.median(p))
print(p1.mean(p))#total/total num
'''
##time
'''
import time,datetime 
print(time.ctime())
print(datetime.datetime.now())
'''
##zlib = compress decompress like encode decode
'''
import zlib
s=b'hello'
print(s)
l=zlib.compress(s)
print(l)
dl=zlib.decompress(l)
print(dl)
'''
##textwrap
'''
import textwrap
d='hello how are you...'
print(textwrap.fill(d,width=5))
op//
hello
how
are y
ou...
'''
