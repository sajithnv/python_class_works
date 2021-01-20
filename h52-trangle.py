from tkinter import *
t=Tk()
c=Canvas(t,width=500,height=500)
##c.create_line(170,170,300,300,width=5,fill='red')
##c.create_line(300,300,50,300,width=5,fill='yellow')
##c.create_line(50,300,170,170,width=5,fill='blue')
p=[170,170,300,300,50,300,170,170]
c.create_polygon(p,outline='blue',fill='red',width=5)
c.pack()
t.mainloop()
