from tkinter import *
from PIL import Image,ImageTk
root=Tk()
# WidthxHeight
root.geometry("450x400")
# width, height
root.maxsize(1920,1080)
#wifdth,height
root.minsize(200,200)

label=Label(text="First GUI text by Sk8 lol")
label.pack()

image=Image.open("img.jpg")
photo=ImageTk.PhotoImage(image)
lb=Label(image=photo)
lb.image=photo
lb.pack()
root.mainloop()