##from tkinter import *
##r=Tk()
##r.geometry('500x500')
##r['bg']='light green'
##l=Listbox(r)
##l.insert(1,'SSLC')
##l.insert(2,'HSS')
##l.insert(3,'UG')
##l.insert(4,'PG')
##l.pack()
##r.mainloop()
from tkinter import *
from tkinter.ttk import Combobox
r=Tk()
r.geometry('500x500')
r['bg']='light green'
c=Combobox(r)
v=('select',8,9,10,11)
c['value']=v
c.current(0)
c.pack()
r.mainloop()
