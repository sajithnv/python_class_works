from tkinter import messagebox as m
from tkinter import *
import time
t=Tk()
t['bg']='light green'
t.geometry('500x500')
t.title('my pgrm')
s=StringVar()
s.set('u r a Male')
def f1():
    s1=s.get()
    m.showinfo(f'Info..',s1)
    time.sleep(2)
    t.withdraw()
r1=Radiobutton(t,text='male',var=s,value='u r a Male',bg='light green')
r2=Radiobutton(t,text='female',var=s,value='u r a Female',bg='light green')
b=Button(t,text='click me',width=30,bg='black',fg='white',command=f1)
r1.pack()
r2.pack()
b.pack()
t.mainloop()
