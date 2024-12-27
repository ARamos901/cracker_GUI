from tkinter import *
from tkinter import filedialog
import hashlib 
import os
import time

def browseFiles():
    global selected_file
    filepath = filedialog.askopenfilename(
        title="Select Wordlist",
        filetypes=(
            ("Text files", "*.txt"),
            ("All files", "*.*")
        )
    )
    if filepath:
        selected_file = filepath
        status_label.config(text=f"Loaded wordlist: {os.path.basename(filepath)}", fg="white")

def Submit():
    global Password
    if not hash_entry.get():
        status_label.config(text="Please enter a hash to crack!", fg="red")
        return
        
    if not selected_file:
        status_label.config(text="Please select a wordlist file!", fg="red")
        return
    
    SubmitButton['state'] = 'disabled'
    SubmitButton['text'] = 'Cracking in Progress...'
    SubmitButton['bg'] = '#756c6b'
    status_label.config(text="Checking hash against wordlist...", fg="yellow")
    window.update()
    
    with open(selected_file, 'r') as file:
        hash_to_check = hash_entry.get()
        for word in file:
            enc_wrd = word.strip().encode('utf-8')
            digest = hashlib.md5(enc_wrd).hexdigest()
            
            if digest == hash_to_check:
                Password = word.strip()
                status_label.config(text=f"The cracked password is: {Password}", fg="white")
                break
        else:
            status_label.config(text="Password could not be cracked with this wordlist", fg="red")
    
    SubmitButton['state'] = 'normal'
    SubmitButton['text'] = 'Click to crack the hash and get your password'
    SubmitButton['bg'] = 'white'

# Main window setup
window = Tk()
window.geometry("600x600")
window.title("Password Cracker")
window.config(background="black")

try:
    lock = PhotoImage(file="unlock.png")
    window.iconphoto(True, lock)
except:
    print("Could not load unlock.png")

# Initialize variables
Password = None
selected_file = None

# Top label
Top = Label(window,
           text="Your personal password cracker",
           fg="white",
           bg="#756c6b",
           relief=RAISED,
           bd=5)
Top.pack(pady=20)

# Hash input section
hash_label = Label(window,
                  text="Enter MD5 Hash:",
                  fg="white",
                  bg="black")
hash_label.pack(pady=5)

hash_entry = Entry(window, 
                  bg="white",
                  width=50)
hash_entry.pack(pady=5)

# Wordlist selection button
browse_button = Button(
    window,
    text="Select Wordlist File",
    command=browseFiles,
    bg="#756c6b",
    fg="black",
    relief=RAISED,
    cursor="hand",
    activebackground="#756c6b",
    activeforeground="white"
)
browse_button.pack(pady=20)

# Submit button
SubmitButton = Button(
    window,
    text="Click to crack the hash and get your password",
    bg="white",
    command=Submit,
    cursor="hand"
)
SubmitButton.pack(pady=20)

# Status area
status_frame = Frame(window, bg="black")
status_frame.pack(pady=20, fill=X, padx=20)

status_label = Label(status_frame,
                    text="Ready to crack...",
                    fg="white",
                    bg="black")
status_label.pack()

window.mainloop()

