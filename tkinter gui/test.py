from tkinter import *
root=Tk()
root.geometry("1920x1080")

f1=Frame(root,bg="light blue")
f1.pack(side=LEFT,fill=Y)

f2=Frame(root,bg="light blue")
f2.pack(side=TOP,fill=X)

lb=Label(f1,text="Welcome to Sk8 editor",bg="GREY",
         font="comicsams 10 bold")
lb.pack()

lb=Label(f2,text="Welcome to My GUI",bg="grey",font="comicsams 10 bold")
lb.pack(anchor="nw")
root.mainloop()