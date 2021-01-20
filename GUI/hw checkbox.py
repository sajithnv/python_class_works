from tkinter import messagebox as m
from tkinter import *
t=Tk()
t.geometry('500x500')
t['bg']='light blue'
s=BooleanVar()
s1=BooleanVar()
s2=BooleanVar()
s3=BooleanVar()
def f1():
    sv=s.get()
    sv1=s1.get()
    sv2=s2.get()
    sv3=s3.get()
    if sv==1:
        m.showinfo('selected..','apple')
        print('apple')
    if sv1==1:
        m.showinfo('selected..','banana')
        print('banana')
    if sv2==1:
        m.showinfo('selected..','grape')
        print('grape')
    if sv3==1:
        m.showinfo('selected..','orange')
        print('orange')    
l=Label(t,text='select ur fav.',width=20)
c1=Checkbutton(t,text='_apple_',bg='light blue',var=s)
c2=Checkbutton(t,text='banana',bg='light blue',var=s1)
c3=Checkbutton(t,text='_grape_',bg='light blue',var=s2)
c4=Checkbutton(t,text='orange',bg='light blue',var=s3)
b=Button(t,text='click here..',width=30,command=f1)
l.pack()
c1.pack()
c2.pack()
c3.pack()
c4.pack()
b.pack()
t.mainloop()
##c1=Checkbutton(t,text='_apple_',bg='light blue',var=s,value='apple')
##c2=Checkbutton(t,text='banana',bg='light blue',var=s,value='banana')
##c3=Checkbutton(t,text='_grape_',bg='light blue',var=s,value='grape')
##c4=Checkbutton(t,text='orange',bg='light blue',var=s,value='orange')
