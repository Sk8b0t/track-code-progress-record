import tkinter
from time import sleep
import threading
import imutils
import cv2
import PIL.Image,PIL.ImageTk
from functools import partial

SET_WIDTH=650
SET_HEIGHT=368

window=tkinter.Tk()
window.title('DECISION REVIEW SYSTEM')

canvas=tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
cv_img=cv2.cvtColor(cv2.imread("welcome.png"),cv2.COLOR_BGR2RGB)
cv_img=imutils.resize(cv_img,width=SET_WIDTH,height=SET_HEIGHT)
cv_img=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
canvas.image=cv_img
canvas.create_image(0,0,image=cv_img,anchor=tkinter.NW)
canvas.pack()
stream=cv2.VideoCapture("clip.mp4")


def play(speed):
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)
    grabbed,frame=stream.read()
    if not grabbed:
        exit()
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    canvas.create_text(120,25,fill="green",font="Times 20 italic bold",text="Decision Pending")


    print(f"the speed of the footsge is {speed}")

def pending(decision):
    #display decision pending logo
    frame=cv2.cvtColor(cv2.imread("pending.png"),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    #wait for a sec
    sleep(1)

    #display out\not out imagef
    if decision =='out':
        img="out.png"
    else:
        img="notout.png"

    frame=cv2.cvtColor(cv2.imread(img),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)


def out():
    thread=threading.Thread(target=(pending),args=("out",))
    thread.daemon=1
    thread.start()
    print("Player is Out")

     
def notOut():
    thread=threading.Thread(target=(pending),args=("not out",))
    thread.daemon=1
    thread.start()
    print("Player is Not Out")

# for adding buttons
btn=tkinter.Button(window,text="Previous(Fast)",width=90,command=partial(play,-25))
btn.pack()

btn=tkinter.Button(window,text="Previous(Slow)",width=90,command=partial(play,-2))
btn.pack()

btn=tkinter.Button(window,text="Next(Fast)",width=90,command=partial(play,25))
btn.pack()

btn=tkinter.Button(window,text="Next(Slow)",width=90,command=partial(play,2))
btn.pack()

btn=tkinter.Button(window,text="Give Out",width=90,command=out)
btn.pack()

btn=tkinter.Button(window,text="Give not out",width=90,command=notOut)
btn.pack()

window.mainloop()