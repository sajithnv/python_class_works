from tkinter import messagebox as m
from tkinter import *
t=Tk()
t.withdraw()
m.showwarning('warning','somthing went wrong')
m.showerror('Error!','there is some ERROR')
m.showinfo('info..','login successfuly')
m.askquestion('msg','are you sure to close this window')
m.askyesno('msg','are you sure??')
m.askokcancel('msg','are you sure??')
m.askyesnocancel('msg','are you sure??')
m.askretrycancel('msg','are you sure??')
t.mainloop()
