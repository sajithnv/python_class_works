from tkinter import *
from tkinter import messagebox as m
r=Tk()
r.geometry('500x500')
st=IntVar()
def fun():
    s1=st.get()
    if s1==1:
        m.showinfo('info','Advance DBMS')
        print('1.Advance DBMS')
    elif s1==2:
        m.showinfo('info','Multimeadia & Animation')
        print('2.Multimeadia & Animation')
    else:
        m.showwarning('alert','Data structure currently not available')
        print('3.Data structure')  
rb1=Radiobutton(r,text='Advance DBMS',variable=st,value=1)
rb2=Radiobutton(r,text='Multimeadia & Animation',variable=st,value=2)
rb3=Radiobutton(r,text='Data structure',variable=st,value=3)
btn=Button(r,text='Click',command=fun)
rb1.pack()
rb2.pack()
rb3.pack()
btn.pack()
r.mainloop()
