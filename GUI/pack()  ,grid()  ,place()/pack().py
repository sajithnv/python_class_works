from tkinter import *
r=Tk()
r.config(bg='light blue')
##r['bg']='light blue'
r.geometry('500x500')
lb1=Label(r,text='abc',font=('sctipt MT bold',20),bg='green')
lb2=Label(r,text='def',font=('times new roman bold',20),bg='red')
lb1.pack()
lb2.pack()
r.mainloop()
