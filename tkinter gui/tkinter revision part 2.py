from tkinter import *
from PIL import Image,ImageTk
import pandas as pd

def dis():
    print(f"username: {n.get()} and password=:{pas.get()}")
    d={"Username":n.get(),
       "password":pas.get()}
    lst.append(d)
    

def showData():
    df=pd.DataFrame(lst)
    print(df)
    df.to_csv("sayan.csv")

if __name__ == "__main__":
    lst=[]
    root=Tk()
    root.geometry("500x450")

    Label(root,text="Username:").grid(row=0,padx=50)
    Label(root,text="password:").grid(row=1,padx=50)

    n=StringVar()
    pas=StringVar()

    Entry(root,textvariable=n).grid(row=0,column=1)
    Entry(root,textvariable=pas,show="*").grid(row=1,column =1)
    
    Button(text="Submit",command=dis).grid(row=2)
    Button(text="Show Data",command=showData).grid(row=2,column=1)
    b3=Button(text="Quit")
    b3.grid(row=2,column=2,padx=32)
    b3.bind("<Button-1>",quit)

    root.mainloop()