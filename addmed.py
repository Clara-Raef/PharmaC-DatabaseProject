from tkinter import *
from tkinter import ttk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector

def back():
    rt.destroy()
    import System
    
def add():
    if mednm1.get()=="" or treat1.get()=="" or form1.get()=="" or medprice1.get()=="" or medst1.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
        Med_name=mednm1.get()
        tr=treat1.get()
        med_form=form1.get()
        med_price=medprice1.get()
        med_stock=medst1.get()
        db=mysql.connector.connect(host="localhost",user="root",password="12345678",database="pharmaC")
        mycursor=db.cursor()
   
    sql="insert into Medicine(Med_name, Treatment,Form,Price,Stock)values(%s,%s,%s,%s,%s)"
    val=(Med_name,tr,med_form,med_price,med_stock)
    mycursor.execute(sql,val)
    db.commit()
    messagebox.showinfo("Done","Medicine added successfully!")
    clearall()
    db.rollback()
    db.close()
    showdata()

def update():
    if mednm1.get()=="":
        messagebox.showerror("Error","Medicine name is required")
    else:
        med_name=mednm1.get()
        tr=treat1.get()
        form_=form1.get()
        med_price=medprice1.get()
        med_stock=medst1.get()
        db=mysql.connector.connect(host="localhost",user="root",password="12345678",database="pharmaC")
        mycursor=db.cursor()
   
    sql="update Medicine set Treatment=%s,Form=%s,Price=%s,Stock=%s where Med_name=%s"
    val=(tr,form_,med_price,med_stock,med_name)
    mycursor.execute(sql,val)
    db.commit()
    messagebox.showinfo("Done","Medicine updated successfully!")
    clearall()
    showdata()
    db.rollback()
    db.close()

def deleteall():
    med_name=mednm1.get()
    db=mysql.connector.connect(host="localhost",user="root",password="12345678",database="pharmaC")
    mycursor=db.cursor()
    sql="delete from Medicine where Med_name=%s"
    val=(med_name)
    mycursor.execute(sql,val)
    db.commit()
    db.close()
    messagebox.showinfo("Done","Medicine deleted from the system.")
    clearall()
    showdata()
        

def clearall():
    mednm1.delete(0,END)
    treat1.delete(0, END)
    form1.delete(0, END)
    medprice1.delete(0, END)
    medst1.delete(0, END)
    supp1.delete(0, END)
    mednm1.focus_set()
    
def search():
    ser1=searchbar.get()
    lsearch1=lsearch.get()
    if(lsearch1=="" or ser1==""):
        messagebox.showerror("Error","Empty Field")
    else:
        db=mysql.connector.connect(host="localhost",user="root",password="12345678",database="pharmaC")
        mycursor=db.cursor()
        mycursor.execute("select * from Medicine where "+str(ser1)+" LIKE '%"+str(lsearch1)+"%'")
        rows=mycursor.fetchall()
        if len(rows)!=0:
            tbdata.delete(*tbdata.get_children())
        for row in rows:
            tbdata.insert('',END,values=[row[1:2],row[0:1],row[2:3],row[3:4],row[4:5],row[5:6],row[6:7],row[7:8]])
        db.commit()
        db.close()
        lsearch.delete(0,END)
        searchbar.delete(0,END)
def showdata():
    med_name=mednm1.get()
    med_exp=treat1.get()
    med_mfd=form1.get()
    med_price=medprice1.get()
    med_stock=medst1.get()
    med_desc=supp1.get()
    db=mysql.connector.connect(host="localhost",user="root",password="12345678",database="pharmaC")
    mycursor=db.cursor()
    mycursor.execute("select * from Medicine")
    rows=mycursor.fetchall()
    if len(rows)!=0:
        tbdata.delete(*tbdata.get_children())
    for row in rows:
        tbdata.insert('',END, values=[row[1:2],row[0:1],row[2:3],row[3:4],row[4:5],row[5:6],row[6:7],row[7:8]])
    db.commit()
    db.close()
def getdata(event):
    currow=tbdata.focus()
    contents=tbdata.item(currow)
    row=contents['values']
    mednm1.delete(0,END)
    treat1.delete(0, END)
    form1.delete(0, END)
    medprice1.delete(0, END)
    medst1.delete(0, END)
    supp1.delete(0, END)
    mednm1.insert(0,row[0])
    treat1.insert(0,row[2])
    form1.insert(0,row[1])
    medprice1.insert(0,row[3])
    medst1.insert(0,row[4])
    supp1.insert(0,row[5])
    

rt=Tk()
rt.geometry("1600x900+0+0")
rt.title("Inventory")
title=Label(rt,text="PHARMA-C",bd=6,relief='raised',font=("Impact",60,"bold"),fg="light sea green",bg="white")
title.pack(side=TOP,fill=X)
backbtn=Button(rt,text="BACK",command=back,bd=5,relief=RAISED,width=7,font=("System",10,"bold"),bg="#755B69",fg="SkyBlue4")
backbtn.place(x=30,y=20,width=90,height=40)
sidefrm=Frame(rt,bd=5,relief=GROOVE,bg="mint cream")
sidefrm.place(x=10,y=100,width=410,height=560)
stitle=Label(sidefrm,text="Update Inventory",font=("Impact",20,"bold"),fg="SkyBlue4",bg="mint cream")
stitle.grid(row=0,columnspan=2,pady=10)
mednm=Label(sidefrm,text="Medicine Name",font=("Monotype Corsiva",16,"bold"),fg="SkyBlue4",bg="mint cream")
mednm.grid(row=1,column=0,padx=20,pady=10,sticky="w")
mednm1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
mednm1.grid(row=1,column=1,padx=20,pady=10,sticky="w")
treat=Label(sidefrm,text="Treatment",font=("Monotype Corsiva",16,"bold"),fg="SkyBlue4",bg="mint cream")
treat.grid(row=2,column=0,padx=20,pady=10,sticky="w")
treat1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
treat1.grid(row=2,column=1,padx=20,pady=10,sticky="w")
form=Label(sidefrm,text="Form",font=("Monotype Corsiva",16,"bold"),fg="SkyBlue4",bg="mint cream")
form.grid(row=3,column=0,padx=20,pady=10,sticky="w")
form1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
form1.grid(row=3,column=1,padx=20,pady=10,sticky="w")
supp=Label(sidefrm,text="Supplier",font=("Monotype Corsiva",16,"bold"),fg="SkyBlue4",bg="mint cream")
supp.grid(row=4,column=0,padx=20,pady=10,sticky="w")
supp1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
supp1.grid(row=4,column=1,padx=20,pady=10,sticky="w")
medprice=Label(sidefrm,text="Medicine Price",font=("Monotype Corsiva",16,"bold"),fg="SkyBlue4",bg="mint cream")
medprice.grid(row=5,column=0,padx=20,pady=10,sticky="w")
medprice1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
medprice1.grid(row=5,column=1,padx=20,pady=10,sticky="w")
medstock=Label(sidefrm,text="Medicine Stock",font=("Monotype Corsiva",16,"bold"),fg="SkyBlue4",bg="mint cream")
medstock.grid(row=6,column=0,padx=20,pady=10,sticky="w")
medst1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
medst1.grid(row=6,column=1,padx=20,pady=10,sticky="w")

addbtn=Button(sidefrm,text="ADD",command=add,bd=5,relief=RAISED,width=11,font=("System",10,"bold")).grid(row=9,column=0,padx=10,pady=10)
addbtn=Button(sidefrm,text="UPDATE",command=update,bd=5,relief=RAISED,width=11,font=("System",10,"bold")).grid(row=9,column=1,padx=10,pady=10)
addbtn=Button(sidefrm,text="DELETE",command=deleteall,bd=5,relief=RAISED,width=11,font=("System",10,"bold")).grid(row=11,column=0,padx=10,pady=10)
addbtn=Button(sidefrm,text="CLEAR",command=clearall,bd=5,relief=RAISED,width=11,font=("System",10,"bold")).grid(row=11,column=1,padx=10,pady=10)

mainfrm=Frame(rt,bd=5,relief=GROOVE,bg="azure2")
mainfrm.place(x=420,y=100,width=720,height=560)
maintitle=Label(mainfrm,text="Medicine Inventory",font=("Sitka Text",20,"bold"),fg="#0F5257",bg="azure2")
maintitle.place(x=190,y=10,width=400,height=40)

searchfrm=Frame(mainfrm,bd=5,relief=FLAT,bg="white")
searchfrm.place(x=5,y=70,width=700,height=450)
searchlb=Label(searchfrm,text="Search By",font=("Monotype Corsiva",18,"bold"),bg="white")
searchlb.grid(row=0,column=0,padx=10,pady=10,sticky="w")
searchbar=ttk.Combobox(searchfrm,width=10,font=("Times New Roman",13,"bold"),state="readonly")
searchbar['values']=("Med_name","Med_id", "Treatment")
searchbar.grid(row=0,column=1,padx=20,pady=10)
lsearch=Entry(searchfrm,font=("Times New Roman",15,"bold"),bd=3,relief=RIDGE)
lsearch.grid(row=0,column=2,pady=10,padx=20,sticky="w")

searchbt=Button(searchfrm,text="SEARCH",command=search,bd=5,relief=RAISED,width=10,font=("System",10,"bold")).grid(row=0,column=4,padx=10,pady=10)
searchbt=Button(searchfrm,text="SHOW ALL",command=showdata,bd=5,relief=RAISED,width=10,font=("System",10,"bold")).grid(row=0,column=5,padx=10,pady=10)

tbframe=Frame(searchfrm,bd=4,relief=RIDGE,bg="#C1CAD6")
tbframe.place(x=20,y=60,width=720,height=360)
scrollx=Scrollbar(tbframe,orient=HORIZONTAL)
scrolly=Scrollbar(tbframe,orient=VERTICAL)
tbdata=ttk.Treeview(tbframe,columns=('Med_name', 'Med_id', 'Form', 'Treatment', 'Price', 'Stock', 'Expiry', 'Supplier'))
scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)
scrollx.config(command=tbdata.xview)
scrolly.config(command=tbdata.yview)
tbdata.heading('Med_name',text="Item name")
tbdata.heading('Med_id',text="Item ID")
tbdata.heading('Form',text="Form")
tbdata.heading('Treatment',text="Treatment")
tbdata.heading('Price',text="Price")
tbdata.heading('Stock',text="Stock left")
tbdata.heading('Expiry',text="Expiry date")
tbdata.heading('Supplier',text="Supplier")
tbdata['show']="headings"
tbdata['show']="headings"
tbdata.column('Med_name',width=120)
tbdata.column('Med_id',width=10)
tbdata.column('Form',width=70)
tbdata.column('Treatment',width=100)
tbdata.column('Price',width=30)
tbdata.column('Stock',width=20)
tbdata.column('Expiry',width=60)
tbdata.column('Supplier',width=60)
tbdata.pack(fill=BOTH,expand=1)
tbdata.bind("<ButtonRelease-1>",getdata)
showdata()
rt.mainloop()