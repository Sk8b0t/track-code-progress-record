from tkinter import *
import tkinter.messagebox as tsmc

def write():
    print("tkintering in tkinter")

def kill():
    a=tsmc.askyesno("Quit","Do you really want to exit?")
    if a:
        root.destroy()

if __name__ == "__main__":
    
    root=Tk()
    root.geometry("500x450")
    root.title("Menus in tkinter")
    menubar=Menu(root)

    m1=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File",menu=m1)
    m1.add_cascade(label="New File",command=write)
    m1.add_cascade(label="New Window",command=write)
    m1.add_separator()

    m4=Menu(menubar,tearoff=0)
    m1.add_cascade(label="File",menu=m4)
    m4.add_cascade(label="Open File...",command=write)
    m4.add_cascade(label="Open Folder...",command=write)


    m2=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Edit",menu=m2)
    m2.add_cascade(label="Undo",command=write)
    m2.add_cascade(label="Redo",command=write)


    m3=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="View",menu=m3)
    m3.add_cascade(label="Quit",command=kill)
    root.config(menu=menubar)


    # root2=Tk()
    # menubar2=Menu(root2)
    # menubar2.add_cascade(label="sayan",command=write)
    # root2.config(menu=menubar2)



    root.mainloop()
