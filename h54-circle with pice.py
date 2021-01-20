from tkinter import *
t=Tk()
c=Canvas(t,width=500,height=500)
c.create_arc(50,50,200,200,start=70,extent=290,fill='yellow',outline='blue',width=3)
c.create_arc(70,40,250,150,start=360,extent=70,fill='red',outline='blue',width=3)
c.pack()
