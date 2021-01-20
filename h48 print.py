from tkinter import *
r=Tk()
r.geometry('500x500')
r['bg']='light blue'
def eyy():
    lb1.config(text='*')
    lb2.config(text='*')
    lb3.config(text='*')   
lb1=Label(r,text='Happy',font=('monospace',30),fg='blue',bg='light blue')
lb2=Label(r,text='Birthday',font=('monospace',30,'italic'),fg='green',bg='light blue')
lb3=Label(r,text='Dr.A P J Abdul Kalam',font=('monospace',30,'bold italic'),fg='red',bg='light blue')
b=Button(r,text='Clear',fg='red',command=eyy,width=20)
lb1.pack()
lb2.pack()
lb3.pack()
b.pack()
r.mainloop()
