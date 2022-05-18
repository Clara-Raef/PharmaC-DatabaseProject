from tkinter import *
from tkinter import ttk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector

def back():
    rt.destroy()
    import System
    
def add():
    if suppnm1.get()=="" or contact1.get()=="" or supply1.get()=="" :
        messagebox.showerror("Error","All fields are required")
    else:
        Supp_name=suppnm1.get()
        cont=contact1.get()
        med_supply=supply1.get()
        db=mysql.connector.connect(host="localhost",user="root",password="12345678",database="pharmaC")
        mycursor=db.cursor()
   
    sql="INSERT INTO Supplier (Supplier_name, Contact, Med_name)values(%s,%s,%s)"
    val=(Supp_name,cont,med_supply)
    mycursor.execute(sql,val)
    db.commit()
    messagebox.showinfo("Done","Supplier added successfully!")
    clearall()
    db.rollback()
    db.close()
    showdata()

def update():
    if suppnm1.get()=="":
        messagebox.showerror("Error","Supplier name is required")
    else:
        Supp_name=suppnm1.get()
        cont=contact1.get()
        supply_=supply1.get()
        db=mysql.connector.connect(host="localhost",user="root",password="12345678",database="pharmaC")
        mycursor=db.cursor()
   
    sql="UPDATE Supplier SET Contact=%s,Med_name=%s"
    val=(Supp_name,cont,supply_)
    mycursor.execute(sql,val)
    db.commit()
    messagebox.showinfo("Done","Supplier updated successfully!")
    clearall()
    showdata()
    db.rollback()
    db.close()

def deleteall():
    Supp_name=suppnm1.get()
    db=mysql.connector.connect(host="localhost",user="root",password="12345678",database="pharmaC")
    mycursor=db.cursor()
    sql="DELETE FROM Supplier WHERE Supplier_name=%s"
    val=(Supp_name)
    mycursor.execute(sql,val)
    db.commit()
    db.close()
    messagebox.showinfo("Done","Supplier deleted from the system.")
    clearall()
    showdata()
        
def clearall():
    suppnm1.delete(0,END)
    contact1.delete(0, END)
    supply1.delete(0, END)
    suppnm1.focus_set()
    
def search():
    ser1=searchbar.get()
    lsearch1=lsearch.get()
    if(lsearch1=="" or ser1==""):
        messagebox.showerror("Error","Empty Field")
    else:
        db=mysql.connector.connect(host="localhost",user="root",password="12345678",database="pharmaC")
        mycursor=db.cursor()
        mycursor.execute("SELECT * FROM Supplier WHERE "+str(ser1)+" LIKE '%"+str(lsearch1)+"%'")
        rows=mycursor.fetchall()
        if len(rows)!=0:
            tbdata.delete(*tbdata.get_children())
        for row in rows:
            tbdata.insert('',END,values=[row[0:1],row[1:2],row[2:3]])
        db.commit()
        db.close()
        lsearch.delete(0,END)
        searchbar.delete(0,END)

def showdata():
    Supp_name=suppnm1.get()
    contact=contact1.get()
    suppmed=supply1.get()
    db=mysql.connector.connect(host="localhost",user="root",password="12345678",database="pharmaC")
    mycursor=db.cursor()
    mycursor.execute("SELECT * FROM Supplier")
    rows=mycursor.fetchall()
    if len(rows)!=0:
        tbdata.delete(*tbdata.get_children())
    for row in rows:
        tbdata.insert('',END, values=[row[0:1],row[1:2],row[2:3]])
    db.commit()
    db.close()

def getdata(event):
    currow=tbdata.focus()
    contents=tbdata.item(currow)
    row=contents['values']
    suppnm1.delete(0,END)
    contact1.delete(0, END)
    supply1.delete(0, END)
    suppnm1.insert(0,row[0])
    contact1.insert(0,row[2])
    supply1.insert(0,row[1])
    

rt=Tk()
rt.geometry("1600x900+0+0")
rt.title("Supplier")
title=Label(rt,text="PHARMA-C",bd=6,relief='raised',font=("Impact",60,"bold"),fg="light sea green",bg="white")
title.pack(side=TOP,fill=X)
backbtn=Button(rt,text="BACK",command=back,bd=5,relief=RAISED,width=7,font=("System",10,"bold"),bg="#755B69",fg="SkyBlue4")
backbtn.place(x=30,y=20,width=90,height=40)
sidefrm=Frame(rt,bd=5,relief=GROOVE,bg="mint cream")
sidefrm.place(x=10,y=100,width=410,height=400)
stitle=Label(sidefrm,text="Update Suppliers List",font=("Impact",20,"bold"),fg="SkyBlue4",bg="mint cream")
stitle.grid(row=0,columnspan=2,pady=10)
suppnm=Label(sidefrm,text="Supplier Name",font=("Monotype Corsiva",16,"bold"),fg="SkyBlue4",bg="mint cream")
suppnm.grid(row=1,column=0,padx=20,pady=10,sticky="w")
suppnm1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
suppnm1.grid(row=1,column=1,padx=20,pady=10,sticky="w")
contact=Label(sidefrm,text="Contact",font=("Monotype Corsiva",16,"bold"),fg="SkyBlue4",bg="mint cream")
contact.grid(row=2,column=0,padx=20,pady=10,sticky="w")
contact1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
contact1.grid(row=2,column=1,padx=20,pady=10,sticky="w")
supply=Label(sidefrm,text="Medicine Supply",font=("Monotype Corsiva",16,"bold"),fg="SkyBlue4",bg="mint cream")
supply.grid(row=3,column=0,padx=20,pady=10,sticky="w")
supply1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
supply1.grid(row=3,column=1,padx=20,pady=10,sticky="w")

addbtn=Button(sidefrm,text="ADD",command=add,bd=5,relief=RAISED,width=11,font=("System",10,"bold")).grid(row=9,column=0,padx=10,pady=10)
addbtn=Button(sidefrm,text="UPDATE",command=update,bd=5,relief=RAISED,width=11,font=("System",10,"bold")).grid(row=9,column=1,padx=10,pady=10)
addbtn=Button(sidefrm,text="DELETE",command=deleteall,bd=5,relief=RAISED,width=11,font=("System",10,"bold")).grid(row=11,column=0,padx=10,pady=10)
addbtn=Button(sidefrm,text="CLEAR",command=clearall,bd=5,relief=RAISED,width=11,font=("System",10,"bold")).grid(row=11,column=1,padx=10,pady=10)

mainfrm=Frame(rt,bd=5,relief=GROOVE,bg="azure2")
mainfrm.place(x=420,y=100,width=720,height=560)
maintitle=Label(mainfrm,text="Suppliers List",font=("Impact",20,"bold"),fg="#0F5257",bg="azure2")
maintitle.place(x=190,y=10,width=400,height=40)

searchfrm=Frame(mainfrm,bd=5,relief=FLAT,bg="white")
searchfrm.place(x=20,y=70,width=650,height=450)
searchlb=Label(searchfrm,text="Search By",font=("Monotype Corsiva",18,"bold"),bg="white")
searchlb.grid(row=0,column=0,padx=10,pady=10,sticky="w")
searchbar=ttk.Combobox(searchfrm,width=15,font=("Times New Roman",13,"bold"),state="readonly")
searchbar['values']=("Supplier_name", "Med_name")
searchbar.grid(row=0,column=1,padx=1,pady=10)
lsearch=Entry(searchfrm,font=("Times New Roman",15,"bold"),bd=3,relief=RIDGE)
lsearch.grid(row=0,column=2,pady=10,padx=20,sticky="w")

searchbt=Button(searchfrm,text="SEARCH",command=search,bd=5,relief=RAISED,width=8,font=("System",10,"bold")).place(x=440,y=10)
searchbt=Button(searchfrm,text="SHOW ALL",command=showdata,bd=5,relief=RAISED,width=8,font=("System",10,"bold")).place(x=550,y=10)

tbframe=Frame(searchfrm,bd=4,relief=RIDGE,bg="#C1CAD6")
tbframe.place(x=50,y=60,width=600,height=360)
scrollx=Scrollbar(tbframe,orient=HORIZONTAL)
scrolly=Scrollbar(tbframe,orient=VERTICAL)
tbdata=ttk.Treeview(tbframe,columns=('Supplier_name', 'Contact', 'Med_name'))
scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)
scrollx.config(command=tbdata.xview)
scrolly.config(command=tbdata.yview)
tbdata.heading('Supplier_name',text="Supplier")
tbdata.heading('Contact',text="Contact")
tbdata.heading('Med_name',text="Medicine Supply")
tbdata['show']="headings"
tbdata.column('Supplier_name',width=120)
tbdata.column('Contact',width=10)
tbdata.column('Med_name',width=70)
tbdata.pack(fill=BOTH,expand=1)
tbdata.bind("<ButtonRelease-1>",getdata)
showdata()
rt.mainloop()