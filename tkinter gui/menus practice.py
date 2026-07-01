from tkinter import *
import tkinter.messagebox as tsmc
def hello():
    print("Hello tkinter")
def kill():
    msg=tsmc.askyesno("Warning","Do you want to Exit?")
    if msg:
        root.destroy()

root=Tk()
root.geometry("600x400")
menubar=Menu(root)
m1=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=m1)
m1.add_command(label="Open File",command=hello)
m1.add_command(label="Open Folder",command=hello)
m1.add_separator()
m2=Menu(m1,tearoff=0)
m1.add_cascade(label="Save",menu=m2)
m2.add_command(label="Save As",command=hello)
m2.add_command(label="Save All",command=hello)
m2.add_command(label="Just Save this",command=hello)
m1.add_separator()
m1.add_command(label="Quit",command=kill)
root.config(menu=menubar)

m3=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=m3)
m3.add_command(label="Undo",command=hello)
m3.add_command(label="Redo",command=hello)
m3.add_separator()
m3.add_command(label="Cut",command=hello)
m3.add_command(label="Copy",command=hello)
m3.add_command(label="Paste",command=hello)
m3.add_separator()
m4=Menu(m3,tearoff=0)
m3.add_cascade(label="Appearance",menu=m4)
m4.add_command(label="Full Screen",command=hello)
m4.add_command(label="Zen Mode",command=hello)
root.config(menu=menubar)





root.mainloop()