##Menu()
from tkinter import *
t=Tk()
t.geometry('500x500')
t.title('menu() in tkinter')
t.resizable(0,0)
t['bg']='light blue'
t['relief']=SOLID
t['bd']=10
def new():
    tm=Tk()
    tm.geometry('500x500')
    tm.title('menu() in tkinter')
    tm.resizable(0,0)
    tm['bg']='light blue'
    tm['relief']=SOLID
    tm.mainloop()
def close():
    t.withdraw()
m=Menu(t)
file=Menu(m,tearoff=0)
file.add_command(label='New File      ctrl+N',command=new)
file.add_command(label='Open..        ctrl+O')
file.add_command(label='Open Module   alt+m')
file.add_command(label='Recent files      >')
file.add_command(label='Exit           ctrl+Q',command=close)
file.add_separator()
file.add_command(label='Save         ctrl+s')
file.add_command(label='Save As      ctrl+sft+s')
edit=Menu(m,tearoff=0)
edit.add_command(label='Undo      ctrl+z')
edit.add_command(label='Rrdo      ctrl+y')
edit.add_separator()
edit.add_command(label='Cut     ctrl+X')
edit.add_command(label='Copy    ctrl+c')
edit.add_command(label='Paste    ctrl+v')
format_=Menu(m,tearoff=0)
format_.add_command(label='Format paragraph')
m.add_cascade(label='File',menu=file)
m.add_cascade(label='Edit',menu=edit)
m.add_cascade(label='format',menu=format_)
t.config(menu=m)

t.mainloop()
