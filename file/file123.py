#file creation in an directory
#f=open('sample.txt','x')
#f.close()
#writing in file
f=open('sample.txt','rb+')
f.write('hello good morning'.encode('utf-8'))
f.seek(0)
print(f.read())
f.close()
#appending
f1=open('sample1.txt','w+')
f1.write('ample')
f1.seek(0)
print(f1.read())
f1.close()
f2=open('sample1.txt','w+')
f2.write('aeple')
f2.seek(0)
print(f2.read())
f2.close()
f3=open('sample1.txt','a+')
f3.write('ap')
f3.seek(0)
print(f3.read())
f3.close()
f4=open('sample4.txt','a+')
print(f4.name)
print(f4.mode)
print(f4.closed)
f4.close()
print(f4.closed)
