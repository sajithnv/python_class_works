from tkinter import *
t=Tk()
c=Canvas(t,width=500,height=500)
p1=[150,150,250,250,50,250]
p2=[70,250,230,250,230,350,70,350,70,250]
c.create_polygon(p1,outline='gray')
c.create_polygon(p2,fill='gray')
c.pack()
