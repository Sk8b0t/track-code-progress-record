from tkinter import *
import tkinter.messagebox as tsmc

def display():
    n=f"You have rated {slider.get()} to our product"
    tsmc.showinfo("Customer Rating",n)
root=Tk()
root.geometry("600x400")
Label(root,text="Customer rating system using sliders")
slider=Scale(root,from_=0, to=5 , orient=HORIZONTAL,tickinterval=2)
slider.pack()
Button(root,text="Submit",command=display).pack()

root.mainloop()