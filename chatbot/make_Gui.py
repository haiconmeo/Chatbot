# -*- coding: utf-8 -*-
# encoding: utf-8
from tkinter import *
 
 
from tkinter import scrolledtext
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')

txt = scrolledtext.ScrolledText(window,width=40,height=10)
txt.insert(INSERT,'mạnh pro vip')
txt.grid(column=0,row=0)
text = Entry(window,width=10)
txt.grid(column=300,row=150)
window.mainloop()