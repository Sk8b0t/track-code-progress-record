from tkinter import *
from PIL import Image,ImageTk
import os

root=Tk()
root.geometry("1920x1080")
path=r"C:\Users\sayan\Pictures\Camera Roll"
lbo=Label(text="The images are :")
lbo.pack()
for i in range(1,13):
    file=f"{i}.jpg"
    image=Image.open(os.path.join(path,file))
    photo=ImageTk.PhotoImage(image)
    lb=Label(image=photo)
    lb.image=photo
    lb.pack()
root.mainloop()