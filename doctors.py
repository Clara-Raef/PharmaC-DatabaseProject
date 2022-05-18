from tkinter import *
from tkinter import ttk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector

def search():
    ser1=searchbar.get()
    lsearch1=lsearch.get()
    if(lsearch1=="" or ser1==""):
        messagebox.showerror("Error","Empty Field")
    else:
        db=mysql.connector.connect(host="localhost",user="root",password="12345678",database="pharmaC")
        mycursor=db.cursor()
        mycursor.execute("SELECT doc_name, shift, clock_in, clock_out from Doctor where "+str(ser1)+" LIKE '%"+str(lsearch1)+"%'")
        rows=mycursor.fetchall()
        if len(rows)!=0:
            tbdata.delete(*tbdata.get_children())
        for row in rows:
            tbdata.insert('',END,values=[row[0:1],row[1:2],row[4:5],row[5:6]])
        db.commit()
        db.close()
        lsearch.delete(0,END)
        searchbar.delete(0,END)

def back():
    rt.destroy()
    import System

def showdata():
    
    db=mysql.connector.connect(host="localhost",user="root",password="12345678",database="pharmaC")
    mycursor=db.cursor()
    mycursor.execute("select * from Doctor")
    rows=mycursor.fetchall()
    if len(rows)!=0:
        tbdata.delete(*tbdata.get_children())
    for row in rows:
        tbdata.insert('',END, values=[row[0:1],row[1:2],row[4:5],row[5:6]])
    db.commit()
    db.close()

def add_doctor():
    rt.destroy()
    import add_doctor

rt=Tk()
rt.geometry("900x600")
imagebg=Image.open("loginbg.jpg")
bg=ImageTk.PhotoImage(imagebg)
bglb=Label(rt,image=bg).place(x=0,y=0,relwidth=1,relheight=1)
rt.title("PharmaC")
title=Label(rt,text="PHARMA-C",bd=6,relief='raised',font=("Impact",60,"bold"),fg="light sea green",bg="white")
title.place(x=100,y=40,width=700,height=70)
backbtn=Button(title,text="BACK",command=back,bd=5,relief=RAISED,width=7,font=("System",10,"bold"),bg="#755B69",fg="cadet blue")
backbtn.place(x=10,y=10,width=90,height=40)
mainfrm=Frame(rt,bd=5,relief=GROOVE,bg="#abdecc")
mainfrm.place(x=50,y=110,width=800,height=450)
add_doc=Button(mainfrm,text="Register new doctor",command=add_doctor,bd=5,relief=RAISED,width=7,font=("System",10,"bold"),bg="#755B69",fg="cadet blue")
add_doc.place(x=80,y=350,width=130,height=40)
searchfrm=Frame(mainfrm,bd=5,relief=SUNKEN,bg="white")
searchfrm.place(x=10,y=10,width=770,height=300)
searchlb=Label(searchfrm,text="Search by",font=("Monotype Corsiva",18,"bold"),fg="light sea green", bg="white")
searchlb.grid(row=0,column=0,padx=10,pady=10,sticky="w")
searchbar=ttk.Combobox(searchfrm,width=10,font=("Times New Roman",13,"bold"),state="readonly")
searchbar['values']=("doc_name", "shift")
searchbar.grid(row=0,column=1,padx=20,pady=10)
lsearch=Entry(searchfrm,font=("Times New Roman",15,"bold"),bd=3,relief=RIDGE)
lsearch.grid(row=0,column=2,pady=10,padx=20,sticky="w")

searchbt=Button(searchfrm,text="SEARCH",command=search,bd=5,relief=RAISED,width=10,font=("System",10,"bold")).grid(row=0,column=4,padx=10,pady=10)

tbframe=Frame(searchfrm,bd=4,relief=RIDGE,bg="#C1CAD6")
tbframe.place(x=20,y=60,width=720,height=200)
tbdata=ttk.Treeview(tbframe,columns=("doc_name","shift","clock_in","clock_out"))
tbdata.heading("doc_name",text="Doctor's Name")
tbdata.heading("shift",text="Shift")
tbdata.heading("clock_in",text="Check-in time")
tbdata.heading("clock_out",text="Check-out time")
tbdata['show']="headings"
tbdata.column("doc_name",width=100)
tbdata.column("shift",width=100)
tbdata.column("clock_in",width=100)
tbdata.column("clock_out",width=100)
tbdata.pack(fill=BOTH,expand=1)
tbdata.bind("<ButtonRelease-1>")
showdata()
rt.mainloop()