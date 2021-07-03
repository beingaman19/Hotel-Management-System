from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk, messagebox
from PIL import Image,ImageTk

rt = Tk()
rt.title("About Us")
rt.geometry("1600x900+0+0")
bg = ImageTk.PhotoImage(file="2.jpg")
bglb9 = Label(rt, image=bg)
bglb9.place(x=0, y=0, relwidth=1, relheight=1)

reg = Label(text="Welcome to Hotel SunShine",font=("Forte", 35), fg="white", bg="black")
reg.place(x=450, y=250, width=700)
aboutfrm = Frame(rt,bd=4, relief=RIDGE, bg="light blue")
aboutfrm.place(x=20, y=100, width=350, height=580)
atitle = Label(aboutfrm,text="About Us",font=("Times New Roman",20,"bold"),fg="brown4",bg="light blue")
atitle.place(x=110,y=10)
abt = Label(aboutfrm,text="Project made by:",font=("Times New Roman",16,"bold"),bg="light blue",fg="black")
abt.place(x=20,y=60)
abt = Label(aboutfrm, text="1. Mayank Kumar Rai", font=("Times New Roman", 14, "bold"), bg="light blue", fg="black")
abt.place(x=20, y=100)
abt = Label(aboutfrm, text="2. Arka Satpati", font=("Times New Roman", 14, "bold"), bg="light blue", fg="black")
abt.place(x=20, y=140)
abt = Label(aboutfrm, text="3. Avirup Banerjee", font=("Times New Roman", 14, "bold"), bg="light blue", fg="black")
abt.place(x=20, y=180)
abt = Label(aboutfrm, text="4. Aman Ranjan", font=("Times New Roman", 14, "bold"), bg="light blue", fg="black")
abt.place(x=20, y=220)
abt = Label(aboutfrm, text="5. Mohan Tulsyan", font=("Times New Roman", 14, "bold"), bg="light blue", fg="black")
abt.place(x=20, y=260)

rt.mainloop()
