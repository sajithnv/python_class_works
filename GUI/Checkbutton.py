from tkinter import messagebox as m
from tkinter import *
t=Tk()
t.geometry('500x500')
t['bg']='light blue'
t.title('message')
#t.wm_iconbitmap('___.ico')
s=IntVar()
def f1():
    m.showwarning('warning',s.get())
def f2():
    t.withdraw()    
l=Label(t,text='familiar with....!')    
l1=Label(t,text='__java_:')
l2=Label(t,text='___c___:')
l3=Label(t,text='___R___:')
l4=Label(t,text='Python:')
l5=Label(t,text='__php__:')
cb1=Checkbutton(t,var=s)
cb2=Checkbutton(t,var=s)
cb3=Checkbutton(t,var=s)
cb4=Checkbutton(t,var=s)
cb5=Checkbutton(t,var=s)
b=Button(t,text='__click__',bg='black',fg='white',command=f1,width=30)
b1=Button(t,text='__Exit__',bg='black',fg='white',command=f2,width=30)
l.grid(column=0,row=0)
l1.grid(column=0,row=1)
l2.grid(column=0,row=2)
l3.grid(column=0,row=3)
l4.grid(column=0,row=4)
l5.grid(column=0,row=5)
cb1.grid(column=1,row=1)
cb2.grid(column=1,row=2)
cb3.grid(column=1,row=3)
cb4.grid(column=1,row=4)
cb5.grid(column=1,row=5)
b.grid(column=2,row=7)
b1.grid(column=2,row=8)
t.mainloop()
