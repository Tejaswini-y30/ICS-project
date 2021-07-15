import tkinter as Tk
from tkinter import ttk

def Decrypt():
    import DecryptFileapp
def Encrypt():
    import EncryptFileapp

win = Tk.Tk() 

label_file_explorer = Tk.Label(win,text = "Welcom To File Encrytpion software",width = 40, height = 2,padx=4, pady=12,fg = "black") 
button_fileEnryption = Tk.Button(win,text = "Decryption",height =2,width=15,command =  Decrypt)
button_ImageEnxcryption = Tk.Button(win,text = "Encryption ",height =2,width=15,command = Encrypt)
button_exit = Tk.Button(win,text = "Exit",height =2,width=10, command = exit)


label_file_explorer.pack()
label_file_explorer.place(x=30,y=5)

button_fileEnryption.pack()
button_fileEnryption.place(x=50,y=90)
button_ImageEnxcryption.pack()
button_ImageEnxcryption.place(x=190,y=90)

button_exit.pack()
button_exit.place(x=150,y=200)

win.config(background = "aquamarine")
win.title("Encryption")
win.geometry("380x300")
win.mainloop()
