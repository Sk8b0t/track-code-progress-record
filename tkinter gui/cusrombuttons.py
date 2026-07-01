from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.geometry("433x634")
root.title("सायन विश्वास")

f2=Frame(root, borderwidth=0,bg="lightblue")
f2.pack(side=TOP)

f1=Frame(root)
f1.pack(fill=X)

def hello():
    print("Tkintering in tkinter")

img=Image.open("img.jpg")
new_img =img.resize((434,317), Image.LANCZOS)
photo=ImageTk.PhotoImage(new_img)

lb=Label(f2,image=photo,bg="lightblue")
lb.pack(side=TOP,anchor=NE,fill=X)

b1=Button(f1,text="Click Me!!",fg="orange", bg="black",command=hello)
b1.pack(fill=X)

b2=Button(f1,text="this button doesnot work",fg="orange", bg="black")
b2.pack(fill=X)

b3=Button(f1,text="this button doesnot work",fg="orange", bg="black")
b3.pack(fill=X)

b4=Button(f1,text="QUIT",fg="orange", bg="black",command=quit)
b4.pack(fill=X)
b4.bind('<Double-Button-1>',quit)


root.mainloop()