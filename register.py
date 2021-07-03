from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
from PIL import Image,ImageTk #pip install Pillow
def login_window():
    rt.destroy()
    import login
def Add():
    if fen.get()=="" or len.get()=="" or cont.get()==""  or email1.get()==""or pass1.get()=="" or pass2=="":
        messagebox.showerror("Error","All fields are required")
    elif pass1.get()!=pass2.get():
        messagebox.showerror("Error", "Password and confirm password must be same")
    elif vag.get()==0:
        messagebox.showerror("Error", "please agree our term and codition")
    else:
     nm=fen.get()
     lm=len.get()
     cont1=cont.get()
     dob1=cal.get()

     gen1=radio.get()
     e=email1.get()
     password1=pass1.get()
     cpass=pass2.get()
     db=mysql.connector.connect(host="localhost",user="root",password="",database="hotel management")
     mycursor=db.cursor()
     try:
        sql="insert into register(FirstName,lastname,phonenumber,dob,gender,emailid,password,confirmpassword)values(%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(nm,lm,cont1,dob1,gen1,e,password1,cpass)
        mycursor.execute(sql,val)
        db.commit()
        lastid=mycursor.lastrowid
        messagebox.showinfo("information","Record Inserted successfully")
        nm.delete(0,END)
        lm.delete(0, END)
        cont1.delete(0, END)
        dob1.delete(0, END)
        gen1.delete(0, END)
        e.delete(0, END)
        password1.delete(0, END)
        cpass.delete(0, END)
        nm.focus_set()
     except None as e:
        print(e)
        db.rollback()
        db.close()

rt=Tk()
rt.title("Register")
rt.geometry("1600x900+0+0")
bg=ImageTk.PhotoImage(file="20.png")
bglb=Label(rt,image=bg)
bglb.place(x=0,y=0,relwidth=1,relheight=1)

reg=Label(text="REGISTER HERE",font=("Georgia",25,"bold"),bg="red")
reg.place(x=20,y=20)
fnm=Label(text="First Name",font=("Times New Roman",15,"bold"),bg="gold")
fnm.place(x=30,y=100)
fen=ttk.Entry(font=("Times New Roman",15))
fen.place(x=30,y=130,width=250)
lnm=Label(text="Last Name",font=("Times New Roman",15,"bold"),bg="gold")
lnm.place(x=370,y=100)
len=ttk.Entry(font=("Times New Roman",15))
len.place(x=370,y=130,width=250)
contact=Label(text="Contact Number",font=("Times New Roman",15,"bold"),bg="gold")
contact.place(x=30,y=170)
cont=ttk.Entry(font=("Times New Roman",15))
cont.place(x=30,y=200,width=250)
dob=Label(text="DOB",font=("Times New Roman",15,"bold"),bg="gold")
dob.place(x=370,y=170)
cal = DateEntry(font=("Times New Roman",15,"bold"),background='gold',foreground='black',borderwidth=2)
cal.place(x=370,y=200,width=250,height=30)

gen=Label(text="Gender",font=("Times New Roman",15,"bold"),bg="gold")
gen.place(x=370,y=250)
radio = StringVar()
m = Radiobutton(text="Male",variable=radio,value="Male",bg="white",font=("Times New Roman",15,"bold"))
m.place(x=370,y=280,width=130,height=20)
f=Radiobutton(text="Female", variable=radio, value="Female",bg="white",font=("Times New Roman",15,"bold"))
f.place(x=370,y=300,width=150,height=20)
email=Label(text="Email",font=("Times New Roman",15,"bold"),bg="gold")
email.place(x=30,y=250)
email1=ttk.Entry(font=("Times New Roman",15))
email1.place(x=30,y=280,width=250)
password=Label(text="Password",font=("Times New Roman",15,"bold"),bg="gold")
password.place(x=30,y=330)
pass1=ttk.Entry(font=("Times New Roman",15))
pass1.place(x=30,y=360,width=250)
pass1.config(show="*")
cnpassword=Label(text="Confirm Password",font=("Times New Roman",15,"bold"),bg="gold")
cnpassword.place(x=370,y=330)
pass2=ttk.Entry(font=("Times New Roman",15))
pass2.place(x=370,y=360,width=250)
pass2.config(show="*")
vag=IntVar()
chk=Checkbutton(variable=vag,text="I Agree to the Terms and Conditions",font=("Times New Roman",10,"bold"),onvalue=1,offvalue=0)
chk.place(x=30,y=440)
b1 = Button(text="Register", command=Add, font=("MS Reference Sans Serif", 15), bg="firebrick1",bd=3,relief="raised",activebackground="gold",activeforeground="black")
b1.place(x=30,y=490)
geg=Label(text="Already have an account?",font=("Times New Roman",11,"bold"),fg="black",bg="gold")
geg.place(x=420,y=440)
b2 = Button(text="Login",command=login_window, font=("MS Reference Sans Serif", 15),bg="firebrick1", bd=3, relief="raised", activebackground="gold", activeforeground="black")
b2.place(x=470,y=490)
rt.mainloop()
