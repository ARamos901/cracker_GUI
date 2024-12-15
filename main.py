#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import filedialog
import hashlib 
import os

window=Tk()

window.geometry("600x600")
window.title("Password Cracker")
window.config(background="black")

lock=PhotoImage(file="unlock.png")
window.iconphoto(True,lock)

label=Label(window,text="Your personal password cracker",
                fg="white",
                bg="#756c6b",
                relief=RAISED,
                bd=5)

label.pack(pady=20)


Hash=Entry()
Hash.pack()


def openFile():
    filepath=filedialog.askopenfilename()
    file=open(filepath,'r')
    for word in file:
        enc_wrd = word.strip().encode('utf-8')
        digest = hashlib.md5(enc_wrd).hexdigest()
        
    file.close()

wordlistButton = Button(
    text="Submit Word List",
    command=openFile,
    activebackground="#756c6b",
    activeforeground="white",
    anchor="center",
    bd=3,
    bg="#756c6b",
    relief=RAISED,
    cursor="hand"
)

wordlistButton.pack(pady=20)




    

window.mainloop()

