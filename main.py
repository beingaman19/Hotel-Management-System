from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk #pip install Pillow
def login_window():
    rt.destroy()
    import login
def reg_win():
    rt.destroy()
    import register
def about_window():
    rt.destroy()
    import about
def exit_window():
    rt.destroy()

rt=Tk()
rt.title("HomePage")
rt.geometry("1600x900+0+0")
bg=ImageTk.PhotoImage(file="2.jpg")
bglb=Label(rt,image=bg)
bglb.place(x=0,y=0,relwidth=1,relheight=1)

reg=Label(text="Welcome to Hotel SunShine",font=("Forte",35),fg="white",bg="black")
reg.place(x=450,y=250,width=700)

b2=Button(text="Login",command=login_window,font=("MS Reference Sans Serif",17),bg="firebrick1",borderwidth=3,relief="raised")
b2.place(x=450,y=330,width=250)
b3 = Button(text="Register", command=reg_win, font=("MS Reference Sans Serif", 17), bg="firebrick1", borderwidth=3, relief="raised")
b3.place(x=450,y=400,width=250)

c1=Button(text="About Us",command=about_window,font=("MS Reference Sans Serif",17),bg="firebrick1",bd=3,relief="raised")
c1.place(x=450,y=470,width=250)
c1 = Button(text="Exit", command=exit_window, font=("MS Reference Sans Serif", 17), bg="firebrick1", bd=3, relief="raised")
c1.place(x=450,y=540, width=250)


rt.mainloop()
