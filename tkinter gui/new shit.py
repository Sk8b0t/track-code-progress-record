from tkinter import *
from PIL import Image,ImageTk

def txtLabel(txt):
    lb=Label(root,text=txt)
    lb.pack()

def photoLabel(img):
    img=Image.open(img)
    photo=ImageTk.PhotoImage(img)
    lb=Label(root,image=photo)
    lb.image=photo
    lb.pack()
    

if __name__=="__main__":
    root=Tk()
    root.geometry("1920x1080")
    txtLabel("tinkering with the tkinter module")
    photoLabel("img.jpg")
    root.mainloop()