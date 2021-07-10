import tkinter
from tkinter import*
from PIL import Image,ImageTk
import os

def __fd__():
    filename="E:\project\OpenCV-Face-Recognition\FacialRecognition/01_face_dataset.py"
    os.system(filename)
    os.system('notepad'+ filename)

def __ft__():
    filename="E:\project\OpenCV-Face-Recognition\FacialRecognition/02_face_training.py"
    os.system(filename)
    os.system('notepad'+ filename)

def __fr__():
    filename="E:\project\OpenCV-Face-Recognition\FacialRecognition/03_face_recognition.py"
    os.system(filename)
    os.system('notepad'+ filename)
    

root=Tk()

root.geometry("900x700+200+50")
root.resizable(False,False)
title=Label(root,text="FacE RecognitioN ApplicatioN",font=("times new roman",30),bg="#0a064f",fg="white")
title.place(x=0,y=0,relwidth =1)

frm=Frame(root,bd=2,relief=RIDGE,bg="white")
frm.place(x=55,y=70,width=790,height=260)


load=Image.open("E:\project\OpenCV-Face-Recognition/assss.png")
render=ImageTk.PhotoImage(load)
img=Label(frm,image=render)
img.place(x=0,y=0)

btn1=Button(root,text="    FaCe DaTaSeT    ",font=("times new roman",20),bd=15,bg="#0a064f",fg="white",command=__fd__)
btn1.place(x=50,y=360)


btn2=Button(root,text="TrAiN DaTaSeT",font=("times new roman",13),bg="#0a064f",bd=15,fg="white",command=__ft__)
btn2.place(x=115,y=450)


btn3=Button(root,text="  FaCe ReCoGnIsE  ",font=("times new roman",20),bg="#0a064f",bd=15,fg="white",command=__fr__)
btn3.place(x=50,y=520)

sahil=Label(root,text="SaHiL ShArMa",bd=20,fg="BlACK",font=("Castellar",30))
sahil.place(x=465,y=490)

ashish=Label(root,text="AsHiSh KuMaR",bd=20,fg="blue",font=("Castellar",30))
ashish.place(x=460,y=550)
root.title("CID")

p1=PhotoImage(file="E:\project\OpenCV-Face-Recognition/images (1).png")
root.iconphoto(False,p1)

bottom=Label(root,text="   ",font=("times new roman",30),bg="#0a064f",fg="red")
bottom.place(x=0,y=660,relwidth =1)

left=Label(root,text="   ",font=("times new roman",30),bg="#0a064f",fg="red",height=14,width=1)
left.pack(side="left")

right=Label(root,text="   ",font=("times new roman",30),bg="#0a064f",fg="red",height=14,width=-1)
right.pack(side="right")

bgimg=Image.open("E:\project\OpenCV-Face-Recognition/download (5).jfif")
test=ImageTk.PhotoImage(bgimg)
label1= tkinter.Label(image=test)
label1.image=test
label1.place(x=490,y=360,height=150,width=350)




root.mainloop()





