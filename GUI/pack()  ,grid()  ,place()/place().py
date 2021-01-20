from tkinter import *
r=Tk()
r.config(bg='light blue')
##r['bg']='light blue'
r.geometry('500x500')
lb1=Label(r,text='abc',font=('sctipt MT bold',20),bg='green')
lb2=Label(r,text='def',font=('times new roman bold',20),bg='red')
lb1.place(x=200,y=200)
lb2.place(x=300,y=300)
##lb1.place(width=700,height=300)
##lb2.place(width=300,height=300)
r.mainloop()
