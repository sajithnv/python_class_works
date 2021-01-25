# insert # delete #update #drop #select #fetchall()
from pymysql import *
d=connect(host='localhost',user='root',password='rooot',database='db1')
c=d.cursor()
##s='drop table if exists new_table'
##c.execute(s)
##print('drop table if exist')
##s1='create table new_table(id integer(20),name varchar(30))'##table creation
##c.execute(s1)
##print('table new_table created')
##s2='insert into new_table values(4,"ith")'
##s3='update new_table set name="ajith" where id=2'
##s4='delete from new_table where name="ajith"'
try:
    s6='delete from new_table values(5,"done")'
    s5='select * from new_table'
##    c.execute(s2)
##    c.execute(s3)
##    c.execute(s4)
    c.execute(s6)
    c.execute(s5)
    result=c.fetchall()
    for i in result:
        print(i[0],i[1])
    d.commit()
    
except:
    d.rollback()
    print('an error')
d.close()

