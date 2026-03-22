from tkinter import *
root=Tk()
root.geometry("450x450")
root.title("Learning events in tkinter ")

def hello(event):
    print("Doing events in tkinter")
    print(f"the co=ordinates which i am working on is with x coordinate:{event.x} and y cordinate:{event.y}")
b1=Button(root,text="Click Me",bg="black",fg="orange")
b1.pack(side=TOP,fill=X)
b1.bind('<Button-1>',hello)
b1.bind('<Double-Button-1>',quit)


root.mainloop()