import tkinter as Tk
from tkinter import ttk



def Files():
    import Fileapp
def Images():
    import imageapp

win = Tk.Tk() 

label_file_explorer = Tk.Label(win,text = "Welcom To Encrytpion software",width = 40, height = 2,padx=4, pady=12,fg = "black") 
button_fileEnryption = Tk.Button(win,text = "File Encryption",height =2,width=15,command = Files)
button_ImageEnxcryption = Tk.Button(win,text = "Image Enxcryption ",height =2,width=15,command = Images)
button_exit = Tk.Button(win,text = "Exit",height =2,width=10, command = exit)


label_file_explorer.pack()
label_file_explorer.place(x=30,y=5)

button_fileEnryption.pack()
button_fileEnryption.place(x=50,y=90)
button_ImageEnxcryption.pack()
button_ImageEnxcryption.place(x=190,y=90)

button_exit.pack()
button_exit.place(x=150,y=200)

win.config(background = "lemon chiffon")
win.title("Encryption")
win.geometry("380x300")
win.mainloop()
