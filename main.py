from tkinter import *
from tkinter import ttk

def login_clicked():
    if (textInputUser.get() == "bodeguero" and textInputPass.get() == "abc123"):
        mainfrm.tkraise()
    else:
        newWindow = Toplevel(root)
        newWindow.title("Error al ingresar")
        newWindow.geometry("150x200")
        Label(newWindow, text ="Usuario o contraseña incorrectos").pack()
        
    

def close():
    frm.tkraise()

root = Tk()
root.geometry("600x400")

mainfrm = ttk.Frame(root, padding=40)
mainfrm.grid(row=0, column=0, sticky="news")
frm = ttk.Frame(root, padding=40)
frm.grid(row=0, column=0, sticky="news")

ttk.Label(frm, text="Iniciar sesión").grid(column=1, row=0)
#ttk.Menubutton = (frm)
textInputUser = StringVar()
textInputPass = StringVar()
ttk.Label(frm, text="Usuario").grid(column=0, row=1)
ttk.Label(frm, text="Contraseña").grid(column=0, row=2)
inputUser = ttk.Entry(frm, textvariable=textInputUser).grid(column=1, row=1)
inputPass = ttk.Entry(frm, textvariable=textInputPass).grid(column=1, row=2)
ttk.Button(frm, text="Ingresar", command=login_clicked).grid(column=1, row=3)

ttk.Label(mainfrm, text="Gestionar").grid(column=1, row=0)
ttk.Button(mainfrm, text="Cerrar sesión", command=close).grid(column=1, row=3)

frm.tkraise()

root.mainloop()