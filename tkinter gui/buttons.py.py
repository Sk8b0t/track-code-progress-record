from tkinter import *


root=Tk()
root.geometry("1280x960")
root.title("NJR")

def hello():
    print("Hello world")


f1=Frame(root,borderwidth=6,bg="grey",height=12,width=12,relief=SUNKEN)
f1.pack(side=LEFT,anchor=NE)

b1=Button(f1,text="PrintMe",fg="orange", command=hello)
b1.pack(side=LEFT)

b2=Button(f1,text="PrintMe",fg="orange")
b2.pack(side=LEFT,padx=9,pady=9)

b3=Button(f1,text="PrintMe",fg="orange")
b3.pack(side=LEFT,padx=9,pady=9)


b4=Button(f1,text="PrintMe",fg="orange")
b4.pack(side=LEFT)

root.mainloop()
    