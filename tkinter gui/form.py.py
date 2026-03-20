from tkinter import *


def write():
    print(f"username:{userValue.get()} password={passValue.get()}")


root=Tk()
root.geometry("456x666")
root.title("Form")

Label(root,text="Username:").grid()
Label(root,text="Password").grid(row=1)

userValue=StringVar()
passValue=StringVar()

userEntry=Entry(root,textvariable=userValue)
userEntry.grid(row=0,column=1)
passEntry=Entry(root, textvariable=passValue)
passEntry.grid(row=1,column=1)

Button(text="Submit",command=write).grid()
root.mainloop()