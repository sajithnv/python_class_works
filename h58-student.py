from pymysql import *
d=connect(host="localhost",user="root",password="rooot",database="db1")
c=d.cursor()
##s1="drop table if exists student1"
##c.execute(s1)
##print('drop student1 if exists')
##s="""create table student1(regno integer(20),stdname varchar(30),maths integer(20),science integer(20),total integer(20),percentage integer(20))"""
##c.execute(s)
##print('Table created successfully')
##s3="insert into student1 values(1004,'abc',30,40,maths+science,(((maths+science)/200)*100))"
s4='select * from student1'
##c.execute(s3)
c.execute(s4)
r=c.fetchall()
print('<<  RGBK TEST RESULTS  >>')
print('__________________________')
for i in r:
    i[0],i[1],i[2],i[3],i[4],i[5]
    if i[5]>=90:
        print(f'Name: {i[1]}\nResult: A grade\nPosition: ** Distinction **\n' )
    elif i[5]>=70 and i[5]<90:
        print(f'Name: {i[1]}\nResult: B grade \nPosition: Average\n')
    elif i[5]>=50 and i[5]<70:
        print(f'Name: {i[1]}\nResult: C grade \nPosition: meduim\n')
    elif i[5]>=35 and i[5]<50:
        print(f'Name: {i[1]}\nResult: D grade\nPosition: just pass\n')
    elif i[5]<35:
        print(f'Name: {i[1]}\nResult: E grade\nPosition:!! FAILED !!!\n ')
print('____________________END of RESULT_______________________________')
print('___RGBK Student details___\n')
for i in r:
    print(f'Student ID     : {i[0]}')
    print(f'Student Name   : {i[1]}')
    print(f'Mark in Maths  : {i[2]}')
    print(f'Mark in Science: {i[3]}')
    print(f'Total Mark     : {i[4]}')
    print('________________________')
print('____________________END of DETAILS______________________________')    
print('****  Program Completed Successfully   ****')    

d.commit()  
#d.rollback()
d.close()
