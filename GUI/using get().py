from tkinter import messagebox as m
from tkinter import *
import time
t=Tk()
t.title('My programm')
t.geometry('500x500')
t['bg']='light green'
def f1():
    s=e.get()
    e.delete(0,END)
    m.showwarning('warning',s)
    time.sleep(2)
    t.withdraw()
e=Entry(t,width=30,font=('times new roman',20))
b=Button(t,text='click',bg='black',fg='white',command=f1)
e.pack()
b.pack()
t.mainloop()
