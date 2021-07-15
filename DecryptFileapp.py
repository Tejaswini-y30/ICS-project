import tkinter as Tk
from tkinter import ttk
from tkinter import filedialog
from AESdecrypt import AESdecrypt_main

global filename
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a txt File",filetypes = (("Text files","*.txt*"),("all files", "*.*")))
    if len(filename) == 0:
        return 
    f = open(filename, "r")
    global file_text
    file_text = f.read()
    if len(filename)>0:
        label_file_explorer.configure(text="File Selected: "+filename)
        print(filename)
        print(f.read())
    else:
        clearFile()


def clearFile():
    label_file_explorer.configure(text ="Please select a text file")


def Next_Step():
    #key=key.get(1.0, "end-1c")
    key = inputtxt.get(1.0, "end-1c")
    myhexstring=AESdecrypt_main(file_text,key)
    print("The output hex value for the entire message is:\n%s\n" % myhexstring)



win = Tk.Tk() 

label_file_explorer = Tk.Label(win,text = "Please select a text file",width = 40, height = 2,padx=4, pady=12,fg = "blue") 
button_explore = Tk.Button(win,text = "Browse Files",height =2,width=10,command = browseFiles)

button_next = Tk.Button(win,text = "Decrypt",height =2,width=10,command = Next_Step)
button_clear = Tk.Button(win,text = "Clear",height =2,width=10,command = clearFile)
button_exit = Tk.Button(win,text = "Exit",height =2,width=10, command = exit)

encryption_technique = Tk.Label(win,text = "Enter 16 character passphrase to encrypt your text file",width = 40, height = 2,padx=10, pady=10,fg = "blue") 
#combo= ttk.Text()
inputtxt=Tk.Text(win,height = 2,width = 30)


label_file_explorer.pack()
label_file_explorer.place(x=30,y=5)

button_clear.pack()
button_clear.place(x=80,y=70)
button_explore.pack()
button_explore.place(x=180,y=70)

encryption_technique.pack()
encryption_technique.place(x=20,y=125)
inputtxt.pack()
inputtxt.place(x=50,y=190)

button_next.pack()
button_next.place(x=180,y=300)
button_exit.pack()
button_exit.place(x=80,y=300)

win.config(background = "mint cream")
win.title("File Encryption")
win.geometry("400x500")
win.mainloop()
