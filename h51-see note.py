from tkinter import *
from tkinter import messagebox as m
r=Tk()
r.geometry('500x500')
def f1():
    r.withdraw()
def f2():
    m.showinfo('Infor...',f'text is: {e.get()}')
    print(e.get())
e=Entry(r,bg='black',fg='white',font=('times new roman',30))
b1=Button(r,text='Quit',command=f1,bg='light blue',fg='Red',width=20)
b2=Button(r,text='show',command=f2,bg='light green',fg='blue',width=20)
e.pack()
b2.pack()
b1.pack()
r.mainloop()
