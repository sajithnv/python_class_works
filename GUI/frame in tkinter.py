##Frame()
from tkinter import *
t=Tk()
t.geometry('500x500')
t['bg']='light blue'
t.title('Frames in tkinter')
t.resizable(0,0)
f1=Frame(t,relief=SOLID,bd=5)
f2=Frame(t,relief=SUNKEN,bd=5)
f3=Frame(t,relief=GROOVE,bd=5)
f4=Frame(t,relief='solid',bd=5)
f1.pack(side=LEFT)
f2.pack(side=LEFT)
f3.pack(side=LEFT)
f4.pack(side=LEFT)
l1=Label(f1,text='\'left side\'')
l2=Label(f2,text='\'left side\'')
l3=Label(f3,text='\'left side\'')
l4=Label(f4,text='\'left side\'')
l1.pack()
l2.pack()
l3.pack()
l4.pack()
t.mainloop()
