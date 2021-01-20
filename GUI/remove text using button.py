from tkinter import *
z=Tk()
def clear():
    l.config(text=' ')
    z.config(bg='black')
    l.config(bg='light blue')
    b1.config(bg='yellow')
z.config(bg='light blue')
z.geometry('500x500')
l=Label(z,text='hi....',width=30,bg='black',fg='red',font=('times new roman',20))
b1=Button(z,text='clear all',command=clear)
l.pack()
b1.pack()
z.mainloop()
