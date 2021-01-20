from tkinter import *
t=Tk()
c=Canvas(t,width=500,height=500)
p=[30,30,160,40,50,100,100,0,140,100,30,30]
c.create_polygon(p,fill='red')
c.pack()
