from tkinter import *
from tkinter import messagebox as m
r=Tk()
r.geometry('500x500')
st=IntVar()
def fun():
    s1=st.get()
    if s1==1:
##        m.showinfo('alert','Advance DBMS')
        print('1.Advance DBMS')
    elif s1==2:
##        m.showinfo('alert','Multimeadia & Animation')
        print('2.Multimeadia & Animation')
    else:
##        m.showinfo('alert','Data structure')
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
