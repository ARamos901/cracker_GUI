#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import filedialog
import hashlib
import os


window=Tk()

window.geometry("600x600")
window.title("Password Cracker")
window.config(background="#756c6b")

lock=PhotoImage(file="unlock.png")
window.iconphoto(True,lock)

label=Label(window,text="Your personal password cracker",
                fg="white",
                bg="#756c6b",
                relief=RAISED,
                bd=5)

label.pack(pady=20)





def openFile():
    filepath=filedialog.askopenfilename()
    file=open(filepath,'r')
    print(file.read())
    file.close()


wordlistButton=Button(text="Submit Word List",command=openFile,
                      bg="#756c6b",
                      fg="white",
                     
                      activebackground="white")
wordlistButton.pack(pady=20)




    

window.mainloop()


