from tkinter import *
import tkinter.messagebox as msgbox

root=Tk()
root.geometry("500x450")
Label( root, text="Retweet?").pack()
E=Entry(root)
E.pack()
print(E.get())
root.mainloop()