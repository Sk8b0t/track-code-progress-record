from tkinter import *
import tkinter.messagebox as tsmc

root=Tk()
root.geometry("700x600")
scBar=Scrollbar(root)
scBar.pack(side=RIGHT,fill=Y)
lstbx=Listbox(root,yscrollcommand=scBar.set)
for i in range(100):
    lstbx.insert(END,f"item:{i}")

lstbx.pack(fill=BOTH)
scBar.config(command=lstbx.yview)


root.mainloop()