from tkinter import *
from PIL import Image,ImageTk
def hello():
    print("Button dabaya toh yeh aayaega")

def eventTaker(event):
    print(f"The x co=ordinate is {event.x} and the y co-rdinate is {event.y}")

root=Tk()
root.geometry("450x440")
root.title("Tkinter Revision")

f1=Frame(root,borderwidth=6,height=33,width=12,bg="black").pack(side=TOP,fill=X)
Label(f1,text="Tkinter revison",bg="black",fg="orange").pack(anchor=NE,fill=X)

f3=Frame(root,bg="black",height=33,width=12).pack(side=LEFT,fill=X)
img=Image.open("sayan.jpg")
new_img =img.resize((500,317), Image.LANCZOS)
photo=ImageTk.PhotoImage(new_img)
Label(f3,image=photo).pack()

f2=Frame(root,borderwidth=0,bg="blue",height=3,width=1).pack(side=TOP)
Button(f2,text="click me",bg="black",fg="orange",command=hello,relief=SUNKEN).pack(fill=X)
b2=Button(text="Click this to see events in tkinter",bg="black",fg="orange",relief=SUNKEN)
b2.pack(fill=X)
b2.bind("<Button-1>",eventTaker)
b2.bind("<Double-Button-1>",quit)





root.mainloop()