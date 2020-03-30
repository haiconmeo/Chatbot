# -*- coding: utf-8 -*-
from tkinter  import *
from tahm_demo import chat2
import tkinter.font
window = Tk()

messages = Text(window)
messages.pack()


input_field = Entry(window ,font="TimesNewRoman")
input_field.pack(side=BOTTOM, fill=X)

def Enter_pressed(event):
    input_get = input_field.get()
    
    messages.insert(INSERT, 'YOUR %s\n' % input_get)
    messages.insert(INSERT, 'TAHM %s\n' % chat2(input_get))
    # label = Label(window, text=input_get)
    
    # label.pack()
    return "break"

frame = Frame(window)  # , width=300, height=300)
input_field.bind("<Return>", Enter_pressed)
frame.pack()

window.mainloop()