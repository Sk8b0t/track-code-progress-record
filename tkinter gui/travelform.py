from tkinter import *
import tkinter.messagebox as tsmc
def write():
    with open("traveldetails.txt","a") as f:
        f.write(f"Name={userValue.get()}\n address={addressValue.get()}\n from={fromVal.get()}\n To={toVal.get()}\n Phone={phoneVal.get()}\n email={emailVal.get()}\n\n")
        print("form data successfully collected!!")
def hello():
    print("Hello Tkinter")

def kill():
    a=tsmc.askyesno("Warning","DO you really want to quit")
    if a :
        root.destroy()


root=Tk() 
root.geometry("400x400")
menubar=Menu(root,tearoff=0)
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

Label(root,text="Welcome to the world of travelling",bg="black",fg="orange",font="comicsenems 12 bold").grid(row=0,column=3)
Label(root,text="Name:").grid()
userValue=StringVar()
Entry(root,textvariable=userValue).grid(row=1,column=3)

Label(root,text="Address").grid(row=2)
addressValue=StringVar()
Entry(root,textvariable=addressValue).grid(row=2,column=3)

Label(root,text="From:").grid(row=3)
fromVal=StringVar()
Entry(root,textvariable=fromVal).grid(row=3,column=3)

Label(root,text="To:").grid(row=4)
toVal=StringVar()
Entry(root,textvariable=toVal).grid(row=4,column=3)

Label(root,text="Phone No:").grid(row=5)
phoneVal=StringVar()
Entry(root,textvariable=phoneVal).grid(row=5,column=3)

Label(root,text="Email").grid(row=6)
emailVal=StringVar()
Entry(root,textvariable=emailVal).grid(row=6,column=3)

foodService=IntVar()
Checkbutton(text="Do you also want to book meals?",variable=foodService).grid(row=7,column=3)

b1=Button(root,text="Submit",command=write,bg="black",fg="orange",padx=1,relief=RAISED)
b1.grid(row=8,column=3)
b1.bind('<Button-1>',quit)

root.mainloop()
