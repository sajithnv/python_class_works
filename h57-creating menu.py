from tkinter import *
t=Tk()
t.geometry('500x500')
f1=Frame(t,relief=SUNKEN,bd=10)
f2=Frame(t,relief=SUNKEN,bd=10)
f3=Frame(t,relief=SUNKEN,bd=10)
f4=Frame(t,relief=SUNKEN,bd=10)
f1.pack(side=LEFT)
f2.pack(side=LEFT)
f3.pack(side=RIGHT)
f4.pack(side=RIGHT)
l1=Button(f1,text="<",font=('times new roman',20),bg='light blue')
l2=Button(f2,text="<",font=('times new roman',20),bg='light blue')
l3=Button(f3,text=">",font=('times new roman',20),bg='light green')
l4=Button(f4,text=">",font=('times new roman',20),bg='light green')
l1.pack()
l2.pack()
l3.pack()
l4.pack()
m=Menu(t)
file=Menu(m,tearoff=0,bg='black',fg='white')
file.add_command(label='Play')
file.add_command(label='pause')
##file.add_command(label='Open Module')
##file.add_command(label='Module Browser')
##file.add_command(label='Path browser')
file.add_separator()
file.add_command(label='backword')
file.add_command(label='forword')

f1=Menu(m,tearoff=0,bg='black',fg='white')
f1.add_command(label='next')
f1.add_command(label='previous')
m.add_cascade(label='Menu1',menu=file,)
m.add_cascade(label='Menu2',menu=f1)
t.config(menu=m)
t.mainloop()
