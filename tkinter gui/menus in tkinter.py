from tkinter import *

def hello():
    print("say hello to menubars in tkinter")
if __name__ == "__main__":
    root=Tk()
    root.geometry("620x400")

    menubar=Menu(root)
    m1=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File",menu=m1)
    m1.add_command(label="Open",command=hello)
    m1.add_command(label="Save As",command=hello)
    m1.add_command(label="Save All",command=hello)
    m1.add_separator()
    m1.add_command(label="Exit tab",command=hello)
    m1.add_command(label="Quit",command=hello)
    root.config(menu=menubar)
    

    m2=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Edit",menu=m2)
    m2.add_command(label="Undo",command=hello)
    m2.add_separator()
    m2.add_command(label="Cut",command=hello)
    m2.add_command(label="Copy",command=hello)
    m2.add_command(label="Paste",command=hello)
    m2.add_separator()
    m3=Menu(m2,tearoff=0)
    m2.add_cascade(label="Click Me",menu=m3)
    m3.add_command(label="This Works tbh")
    m3.add_command(label="This Works tbh x2",command=quit)
    root.config(menu=menubar)


    # menubar2=Menu(root,tearoff=0)
    # root.config(menu=menubar2)
    # menubar2.add_cascade(label="Shit", menu=m2)
    

    root.mainloop()