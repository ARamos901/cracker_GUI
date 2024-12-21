from tkinter import *
from tkinter import filedialog
import hashlib 
import os
import time

window=Tk()

window.geometry("600x600")
window.title("Password Cracker")
window.config(background="black")

lock=PhotoImage(file="unlock.png")
window.iconphoto(True,lock)

Top=Label(window,text="Your personal password cracker",
                fg="white",
                bg="#756c6b",
                relief=RAISED,
                bd=5)

Top.pack(pady=20)


Hash=Entry()
Hash.pack()

Password=None
def openFile():
    filepath=filedialog.askopenfilename()
    time.sleep(3)
       
    for word in file:
        enc_wrd = word.strip().encode('utf-8')
        digest = hashlib.md5(enc_wrd).hexdigest()
        
        if digest == Hash:
            Password=word.strip()
            break
        
        
    file.close()

message=None

def Message():
    if Password!=None:
        message=f"The cracked password is {Password}."
    else:
        message="The Password could not be cracked."

Message()     

def AddPass():
    DisplayPass.insert(END,message)

DisplayPass=Label(window,text="Cracked Password will be appear here.")





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

