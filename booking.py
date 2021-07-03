
from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
from PIL import Image,ImageTk #pip install Pillow
def home_win():
    rt.destroy()

rt=Tk()
rt.title("Booking")
rt.geometry("1600x900+0+0")
title=Label(rt,text="Welcome to Hotel Sunshine",bd=10,relief=GROOVE,font=("Forte",35,"bold"),fg="black",bg="gold")
title.pack(side=TOP,fill=X)
mangefrm=Frame(rt,bd=4,relief=RIDGE,bg="wheat1")
mangefrm.place(x=20,y=100,width=450,height=580)
mtitle = Label(mangefrm, text="Customer Info", font=("Goudy Old Style",20,"bold"),fg="brown4",bg="wheat1")
mtitle.grid(row=0,columnspan=2,pady=20)
icd=Label(mangefrm,text="Name:",font=("Times New Roman",15,"bold"),bg="wheat1")
icd.grid(row=1,column=0,pady=10,padx=20,sticky="w")
icd1=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
icd1.grid(row=1,column=1,pady=10,padx=20,sticky="w")
inm=Label(mangefrm,text="Contact Number:",font=("Times New Roman",15,"bold"),bg="wheat1")
inm.grid(row=2,column=0,pady=10,padx=20,sticky="w")
inm1=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
inm1.grid(row=2,column=1,pady=10,padx=20,sticky="w")
unitp=Label(mangefrm,text="Checkin Date:",font=("Times New Roman",15,"bold"),bg="wheat1")
unitp.grid(row=3,column=0,pady=10,padx=20,sticky="w")
unitp1 = DateEntry(mangefrm, font=("Times New Roman", 15, "bold"), bd=5, relief=GROOVE,bg="gold", fg="black")
unitp1.grid(row=3,column=1,pady=10,padx=20,sticky="w")
qty=Label(mangefrm,text="Checkout Date:",font=("Times New Roman",15,"bold"),bg="wheat1")
qty.grid(row=4,column=0,pady=10,padx=20,sticky="w")
qty1=DateEntry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE,bg="gold",fg="black")
qty1.grid(row=4,column=1,pady=10,padx=20,sticky="w")
unit1=Label(mangefrm,text="Room Number:",font=("Times New Roman",15,"bold"),bg="wheat1")
unit1.grid(row=5,column=0,pady=10,padx=20,sticky="w")
unit2=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
unit2.grid(row=5,column=1,pady=10,padx=20,sticky="w")
bill=Label(mangefrm,text="Total Bill:",font=("Times New Roman",15,"bold"),bg="wheat1")
bill.grid(row=6,column=0,pady=10,padx=20,sticky="w")
bill2=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
bill2.grid(row=6,column=1,pady=10,padx=20,sticky="w")
pay=Label(mangefrm,text="Payment:",font=("Times New Roman",15,"bold"),bg="wheat1")
pay.grid(row=7,column=0,pady=10,padx=20,sticky="w")
radio = StringVar()
pay1= Radiobutton(mangefrm,text="Paid",variable=radio,value="Paid",bg="white",font=("Times New Roman",12,"bold"))
pay1.grid(row=7,column=1,pady=10,padx=20,sticky="w")
pay2=Radiobutton(mangefrm,text="Not Paid", variable=radio, value="Not Paid",bg="white",font=("Times New Roman",12,"bold"))
pay2.grid(row=8,column=1,pady=10,padx=20,sticky="w")
btnfrm=Frame(mangefrm,bd=4,relief="ridge",bg="black")
btnfrm.place(x=17,y=510,width=407,height=50)
def add():
    if icd1.get()=="" or inm1.get()=="" or unitp1.get()=="" or qty1.get()=="" or unit2.get()=="" or bill2.get()=="":
       messagebox.showerror("Error","All fields are required")
    else:
     ic=icd1.get()
     nm=inm1.get()
     up=unitp1.get()
     qt=qty1.get()
     pac=unit2.get()
     bill = bill2.get()
     pay = radio.get()

     db=mysql.connector.connect(host="localhost",user="root",password="",database="hotel management")
     mycursor=db.cursor()
     try:
        sql="insert into booking(Name,PhoneNumber,CheckinDate,CheckoutDate,RoomNumber,Bill,Payment)values(%s,%s,%s,%s,%s,%s,%s)"
        val=(ic,nm,up,qt,pac,bill,pay)
        mycursor.execute(sql,val)
        db.commit()
        messagebox.showinfo("information","Record Inserted successfully")
        fectdata()
        cleardata()
     except EXCEPTION as e:
        print(e)
        db.rollback()
        db.close()
def fectdata():
    ic = icd1.get()
    nm = inm1.get()
    up = unitp1.get()
    qt = qty1.get()
    pac = unit2.get()
    bill=bill2.get()
    pay = radio.get()
    db = mysql.connector.connect(host="localhost", user="root", password="", database="hotel management")
    mycursor = db.cursor()
    mycursor.execute("select * from booking")
    rows=mycursor.fetchall()
    if len(rows)!=0:
        medtab.delete(*medtab.get_children())
    for row in rows:
       medtab.insert('',END,values=row)
    db.commit()
    db.close()
def cleardata():
    icd1.delete(0, 'end')
    inm1.delete(0, 'end')
    unitp1.delete(0, 'end')
    qty1.delete(0, 'end')
    unit2.delete(0 ,'end')
    bill2.delete(0, 'end')

    icd1.focus_set()
def getdata(event):
    currow=medtab.focus()
    contents=medtab.item(currow)
    row=contents['values']
    icd1.delete(0, END)
    inm1.delete(0, END)
    unitp1.delete(0, END)
    qty1.delete(0, END)
    unit2.delete(0, END)
    bill2.delete(0, END)


    icd1.insert(0,row[0])
    inm1.insert(0,row[1])
    unitp1.insert(0,row[2])
    qty1.insert(0,row[3])
    unit2.insert(0,row[4])
    bill2.insert(0, row[5])



def update():
    ic = icd1.get()
    nm = inm1.get()
    up = unitp1.get()
    qt = qty1.get()
    pac = unit2.get()
    bill=bill2.get()
    pay = radio.get()
    db = mysql.connector.connect(host="localhost", user="root", password="", database="hotel management")
    mycursor = db.cursor()
    try:
        sql = "update booking set PhoneNumber=%s,CheckinDate=%s,CheckoutDate=%s,RoomNumber=%s,Bill=%s,Payment=%s where Name=%s"
        val = (nm, up, qt, pac,bill,pay, ic)
        mycursor.execute(sql,val)
        db.commit()
        messagebox.showinfo("information", "Record Updated successfully")
        icd1.delete(0, END)
        inm1.delete(0, END)
        unitp1.delete(0, END)
        qty1.delete(0, END)
        unit2.delete(0, END)
        bill2.delete(0, END)


        fectdata()
        cleardata()
    except EXCEPTION as e:
        print(e)
        db.rollback()
        db.close()
def delete1():
    ic = icd1.get()
    db = mysql.connector.connect(host="localhost", user="root", password="", database="hotel management")
    mycursor = db.cursor()
    try:
        sql = "delete from booking where Name=%s"
        val = (ic,)
        mycursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("information", "Record Deleted successfully")
        icd1.delete(0, END)
        inm1.delete(0, END)
        unitp1.delete(0, END)
        qty1.delete(0, END)
        unit2.delete(0, END)
        bill2.delete(0, END)

        fectdata()
        cleardata()
    except EXCEPTION as e:
        print(e)
        db.rollback()
        db.close()
def fectdata1():
    ser1=comboser.get()
    lsearch1 = lsearch.get()
    db = mysql.connector.connect(host="localhost", user="root", password="", database="hotel management")
    mycursor = db.cursor()
    mycursor.execute("select * from booking where "+str(ser1)+" LIKE '%"+str(lsearch1)+"%'")
    rows=mycursor.fetchall()
    if len(rows)!=0:
        medtab.delete(*medtab.get_children())
    for row in rows:
       medtab.insert('',END,values=row)
    db.commit()
    db.close()

addbt=Button(btnfrm,text="ADD",command=add,width=10,bg="firebrick1",bd=3,relief="raised").grid(row=0,column=1,padx=8,pady=10)
updatebt = Button(btnfrm, text="UPDATE", command=update, width=10, bg="firebrick1",bd=3, relief="raised").grid(row=0, column=2, padx=9, pady=10)
detebt = Button(btnfrm, text="DELETE", command=delete1, width=10, bg="firebrick1",bd=3, relief="raised").grid(row=0, column=3, padx=10, pady=10)
clrt = Button(btnfrm, text="CLEAR", command=cleardata, width=10, bg="firebrick1",bd=3, relief="raised").grid(row=0, column=4, padx=9, pady=10)
detfrm=Frame(rt,bd=4,relief=RIDGE,bg="wheat1")
detfrm.place(x=490,y=100,width=770,height=580)
lsearch=Label(detfrm,text="Search By",font=("Times New Roman",16,"bold"),bg="wheat1")
lsearch.grid(row=0,column=0,pady=8,padx=20,sticky="w")
comboser=ttk.Combobox(detfrm,width=14,font=("Times New Roman",12,"bold"),state='readonly')
comboser['values']=("Name","RoomNumber","PhoneNumber")
comboser.grid(row=0,column=1,padx=20,pady=10)
lsearch=Entry(detfrm,font=("Times New Roman",12,"bold"),bd=5,relief="groove")
lsearch.grid(row=0,column=2,pady=10,padx=18,sticky="w")
serbt=Button(detfrm,text="Search",command=fectdata1,font=("Times New Roman",10,"bold"),width=12,pady=5,bg="firebrick1",activebackground="gold",bd=3,relief="raised").grid(row=0,column=3,padx=10,pady=10)
showbt=Button(detfrm,text="Show All",command=fectdata,font=("Times New Roman",10,"bold"),width=12,pady=5,bg="firebrick1",activebackground="gold",bd=3,relief="raised").grid(row=0,column=4,padx=10,pady=10)
b3 = Button(detfrm,text="Exit",command=home_win,font=("Times New Roman",10, "bold"), width=12, pady=5,bg="firebrick1",bd=3,relief="raised",activebackground="gold")
b3.place(x=340,y=530)
tabfrm=Frame(detfrm,bd=4,relief=RIDGE,bg="brown4")
tabfrm.place(x=8,y=70,width=750,height=450)
scrollx=Scrollbar(tabfrm,orient=HORIZONTAL)
scrolly=Scrollbar(tabfrm,orient=VERTICAL)
medtab=ttk.Treeview(tabfrm,columns=("icode","name","up1","qyty","units","bills","pays"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)
scrollx.config(command=medtab.xview)
scrolly.config(command=medtab.yview)
medtab.heading("icode",text="Name")
medtab.heading("name",text="Phone no")
medtab.heading("up1",text="Checkin")
medtab.heading("qyty",text="Checkout")
medtab.heading("units",text="Room no")
medtab.heading("bills",text="Total Bill")
medtab.heading("pays",text="Payment")
medtab['show']="headings"
medtab.column("icode",width=100)
medtab.column("name",width=100)
medtab.column("up1",width=100)
medtab.column("qyty",width=100)
medtab.column("units",width=100)
medtab.column("bills",width=100)
medtab.column("pays",width=100)
medtab.pack(fill=BOTH,expand=1)
medtab.bind("<ButtonRelease-1>",getdata)
fectdata()

rt.mainloop()





