from tkinter import messagebox as m
from tkinter import *
r=Tk()
r['bg']='light green'
r.geometry('500x500')
def f1():
    b.config(bg='light green')    
    r.config(bg='light blue')
    m.showinfo('infor...','button clicked')
    b.config(bg='light green')
b=Button(r,text='BUTTON',fg='red',font=('script MT bold',20),bg='light blue',width=10,command=f1)
b.pack(pady=5)
