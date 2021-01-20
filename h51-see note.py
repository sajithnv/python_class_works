from tkinter import *
from tkinter import messagebox as m
r=Tk()
r.geometry('500x500')
def f1():
    r.withdraw()
def f2():
    print(e.get())
e=Entry(r,width=20)
b1=Button(r,text='Quit',command=f1)
b2=Button(r,text='show',command=f2)
e.grid(column=0,row=0)
b1.grid(column=0,row=1)
b2.grid(column=1,row=1)
r.mainloop()
