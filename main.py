from tkinter import * 

root = Tk()
root.geometry("600x400")
frame = Frame(root)
frame.pack()
 
leftframe = Frame(root)
leftframe.pack(side=LEFT)
 
rightframe = Frame(root)
rightframe.pack(side=RIGHT)
 
label = Label(frame, text = "Ingresar")
label.pack()

my_entry = Entry(frame, width = 20)
my_entry.insert(0,'Usuario')
my_entry.pack(padx = 5, pady = 5)
 
my_entry2 = Entry(frame, width = 15)
my_entry2.insert(0,'Contraseña')
my_entry2.pack(padx = 5, pady = 5)

button1 = Button(frame, text = "Ingresar")
button1.pack(padx = 3, pady = 3)
 
root.title("Libreria")
root.mainloop()