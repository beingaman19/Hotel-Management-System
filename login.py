from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
from PIL import Image,ImageTk #pip install Pillow
def register_win():
    rt.destroy()
    import register

def sel():
    if email1.get()=="" or password.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
        nm = email1.get()
        pwd2 = password.get()
        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", database="hotel management")
            mycursor = db.cursor()
            mycursor.execute("select * from register where emailid=%s and password=%s",(nm,pwd2))
            row = mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid EmailId or Password")
            else:
              messagebox.showinfo("Success", "Welcome")
              rt.destroy()
              import home

            db.commit()    
        except EXCEPTION as es:
                print(es)
    db.rollback()
    db.close()
rt=Tk()
rt.title("LoginPage")
rt.geometry("1600x900+0+0")
bg=ImageTk.PhotoImage(file="13.png")
bglb=Label(rt,image=bg)
bglb.place(x=0,y=0,relwidth=1,relheight=1)
bg1=ImageTk.PhotoImage(file="16.jpg")
logolb=Label(rt,image=bg1)
logolb.place(x=20,y=105,width=360,height=500)
bg9=ImageTk.PhotoImage(file="16.jpg")
logolb=Label(rt,image=bg9)
logolb.place(x=890,y=105,width=360,height=500)

reg=Label(text="Hotel SunShine",font=("Forte",30),fg="black",bg="cyan1")
reg.place(x=425,y=50,width=420)
reg=Label(text="Login for Booking",font=("Times New Roman",24,"bold"),fg="darkgreen")
reg.place(x=510,y=150)
mailid=Label(text="Enter Email Id",font=("Calisto MT",15,"bold"),bg="black",fg="white")
mailid.place(x=562,y=240)
email1=ttk.Entry(font=("MS Reference Sans Serif",13))
email1.place(x=513,y=280,width=250)
pwd=Label(text="Password",font=("Calisto MT",15,"bold"),bg="black",fg="white")
pwd.place(x=583,y=350)
password=ttk.Entry(font=("MS Reference Sans Serif",13))
password.place(x=510,y=390,width=250)
password.config(show="*")
b1 = Button(text="Login", command=sel, font=("MS Reference Sans Serif", 15, "bold"), bg="red", bd=3, relief="raised")
b1.place(x=590,y=450)
ceg=Label(text="Don't have an account?",font=("Times New Roman",12,"bold"),bg="gold")
ceg.place(x=550,y=540)
reg=Button(text="New Account",command=register_win,font=("MS Reference Sans Serif",15,"bold"),bg="red",bd=3,relief="raised")
reg.place(x=550,y=580)

rt.mainloop()


