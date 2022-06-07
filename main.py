from tkinter import *
from tkinter import ttk

def login_clicked():
    print(textInputUser.get())

root = Tk()
root.geometry("600x400")
frm = ttk.Frame(root, padding=40)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Menubutton = (frm)
textInputUser = StringVar()
textInputPass = StringVar()
inputUser = ttk.Entry(frm, textvariable=textInputUser).grid(column=0, row=1)
inputPass = ttk.Entry(frm, textvariable=textInputPass).grid(column=0, row=3)
ttk.Button(frm, text="Login", command=login_clicked).grid(column=0, row=4)
root.mainloop()