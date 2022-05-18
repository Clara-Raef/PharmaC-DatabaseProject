from tkinter import *
from tkinter import ttk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
from datetime import datetime
import mysql.connector

def inventory():
    rt.destroy
    import addmed

def doctor():
    rt.destroy()
    import doctors

def supplier():
    rt.destroy()
    import supplier_list

def logout():
    rt.destroy()
    import Login

rt=Tk()
rt.title("Welcome to Pharma-C")
rt.geometry("900x600")
imagebg=Image.open("loginbg.jpg")
bg=ImageTk.PhotoImage(imagebg)
bglb=Label(rt,image=bg).place(x=0,y=0,relwidth=1,relheight=1)
#-------------------LABEL----------------------------
title=Label(rt,text="PHARMA-C",bd=6,relief='raised',font=("Impact",60,"bold"),fg="light sea green",bg="white")
title.place(x=100,y=40,width=700,height=70)
#-------------------FRAME----------------------------
topframe=Frame(rt,bd=5,relief='raised',bg="white")
topframe.place(x=350,y=110,width=210,height=450)
#-------------------DATE&TIME------------------------
now = datetime.now()
dt_string = now.strftime("%a %d/%m/%Y %H:%M:%S")
_now_label=Label(rt, text=dt_string, fg="SkyBlue4" ,bg="white").place(x=630, y=80)
#-------------------MENU-----------------
btnframe=Frame(topframe,bd=5,relief=RIDGE,bg="#d3d3d3")
btnframe.place(x=10,y=10,width=180,height=410)
medicine=Button(btnframe,text="Inventory",command=inventory, bd=5,relief=RAISED,font=("System",10,"bold")).place(x=0,y=0,width=170,height=70)
orders=Button(btnframe,text="Orders",bd=5,relief=RAISED,font=("System",10,"bold")).place(x=0,y=70,width=170,height=70)
cart_=Button(btnframe,text="Cart",bd=5,relief=RAISED,font=("System",10,"bold")).place(x=0,y=140,width=170,height=70)
supplier=Button(btnframe,text="Suppliers",command=supplier, bd=5,relief=RAISED,font=("System",10,"bold")).place(x=0,y=210,width=170,height=70)
doctor_=Button(btnframe,text="Doctors",command=doctor,bd=5,relief=RAISED,font=("System",10,"bold")).place(x=0,y=280,width=170,height=70)
logout_=Button(btnframe,text="LOGOUT",command=logout,bd=5,relief=RAISED,font=("System",10,"bold")).place(x=0,y=350,width=170,height=50)

rt.mainloop()