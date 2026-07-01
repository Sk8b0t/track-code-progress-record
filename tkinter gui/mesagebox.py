from tkinter import *
import tkinter.messagebox as tmsg

def msgBox():
    a=tmsg.showwarning("Warning","You are about to quit tis application")
    if a:
        root.destroy()
if __name__ == "__main__":
    root=Tk()
    root.geometry("620x400")
    menubar=Menu(root,tearoff=0)
    m1=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File",menu=m1)
    m1.add_command(label="Quit",command=msgBox)
    root.config(menu=menubar)

    root.mainloop()
