from tkinter import *

def write():
    with open("traveldetails.txt","a") as f:
        f.write(f"Name={userValue.get()}\n address={addressValue.get()}\n from={fromVal.get()}\n To={toVal.get()}\n Phone={phoneVal.get()}\n email={emailVal.get()}\n\n")
        print("form data successfully collected!!")

root=Tk()   
root.geometry("400x400")
Label(root,text="Welcome to the world of travelling",bg="black",fg="orange",font="comicsenems 12 bold").grid(row=0,column=3)
Label(root,text="Name:").grid()
userValue=StringVar()
Entry(root,textvariable=userValue).grid(row=1,column=3)

Label(root,text="Address").grid(row=2)
addressValue=StringVar()
Entry(root,textvariable=addressValue).grid(row=2,column=3)

Label(root,text="From:").grid(row=3)
fromVal=StringVar()
Entry(root,textvariable=fromVal).grid(row=3,column=3)

Label(root,text="To:").grid(row=4)
toVal=StringVar()
Entry(root,textvariable=toVal).grid(row=4,column=3)

Label(root,text="Phone No:").grid(row=5)
phoneVal=StringVar()
Entry(root,textvariable=phoneVal).grid(row=5,column=3)

Label(root,text="Email").grid(row=6)
emailVal=StringVar()
Entry(root,textvariable=emailVal).grid(row=6,column=3)

foodService=IntVar()
Checkbutton(text="Do you also want to book meals?",variable=foodService).grid(row=7,column=3)

Button(root,text="Submit",command=write,bg="black",fg="orange",padx=1,relief=RAISED).grid(row=8,column=3)

root.mainloop()
