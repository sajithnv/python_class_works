f=open('h_32_print_lastline.txt','a+')
##f.truncate(0) #this is used to empty the file
##f.write('hi\nhello\nwelcome')
f.seek(0)
##print(f.read())
f.seek(0)
p2=f.readline()
p1=f.readline()
p=f.readline()
print(p)
f.close()
