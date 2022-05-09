from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

def login_function():
        if txtuser.get()==""or txtpass.get()=="":
            messagebox.showerror("Error", "Please enter both username & password")
        else:
            user_name=txtuser.get()
            user_pass=txtpass.get()
            try:
                db=mysql.connector.connect(host="localhost",user="root",password="12345678",database="pharmaC")
                mycursor=db.cursor()
                mycursor.execute("SELECT * from Doctor WHERE username=%s and _password_=%s",(user_name,user_pass))
                row=mycursor.fetchone()
                if row==None:
                    messagebox.showerror("Try again","Invalid username and/or password")
                else:
                    messagebox.showinfo("Welcome!","Login successful!")
                    rt.destroy()
                    import System
                    
            except EXCEPTION as e:
                 print(e)
            db.rollback()
            db.close()

rt=Tk()
rt.title("PharmaC")
rt.geometry("800x700")

photo=Image.open("loginbg.jpg")
bg=ImageTk.PhotoImage(photo)
lbl_bg=Label(rt,image=bg)
lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
                #====Login Frame=====
frame=Frame(rt,bg="white", highlightbackground="cadet blue", highlightthickness="5")
frame.place(x=150,y=150,height=400,width=500)


title=Label(frame,text="PHARMA-C",font=("Impact",60,"bold"),fg="light sea green",bg="white")
title.place(x=140,y=30)

username=Label(frame,text="User Email",font=("Goudy old style",15,"bold"),fg="gray",bg="white")
username.place(x=118,y=140)

txtuser=Entry(frame,font=("times new roman",15),bg="lightgray")
txtuser.place(x=90,y=170,width=350,height=35)

password=Label(frame,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white")
password.place(x=118,y=210)

txtpass=Entry(frame,font=("times new roman",15),bg="lightgray")
txtpass.place(x=90,y=240,width=350,height=35)
txtpass.config(show="*")

                #====icon======
img2=Image.open("userpic.png")
img2=img2.resize((25,25),Image.ANTIALIAS)
photoimage2=ImageTk.PhotoImage(img2)
lblimg1=Label(image=photoimage2,bg="white",borderwidth=0)
lblimg1.place(x=238,y=290,width=25,height=25)

img3=Image.open("passwordpic.png")
img3=img3.resize((25,25),Image.ANTIALIAS)
photoimage3=ImageTk.PhotoImage(img3)
lblimg2=Label(image=photoimage3,bg="white",borderwidth=0).place(x=238,y=362,width=25,height=25)

loginbtn=Button(frame,command=login_function,text="Login",cursor="hand2",fg="black",bg="#d77337",font=("helvetica",16)).place(x=220,y=290)

              
rt.mainloop()