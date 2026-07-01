from tkinter import *
def add():
    global i
    lstbox.insert(END,f"{i}th line in the listbox")
    i+=1

root=Tk()
i=0
root.geometry("600x400")
root.title("ListBox in tkinter")
lstbox=Listbox(root)
lstbox.pack()
lstbox.insert(ACTIVE,"LINES in the listbox")
Button(root,text="Add More",command=add).pack()
root.mainloop()