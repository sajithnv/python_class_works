from tkinter import *
r=Tk()
r.geometry('500x500')
r.config(bg='light blue')
lb1=Label(r,text='abc',font=('script MT bold',20),bg='green')
lb2=Label(r,text='def',font=('times new roman',20),bg='red')
lb1.grid(column=0,row=0)
lb2.grid(column=1,row=1)
r.mainloop()
