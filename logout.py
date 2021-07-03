from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk #pip install Pillow
def main_window():
    rt.destroy()
    import main
def home_win():
    rt.destroy()
    import home

rt=Tk()
rt.title("Logout Page")
rt.geometry("1600x900+0+0")
bg=ImageTk.PhotoImage(file="20.jpg")
bglb=Label(rt,image=bg)
bglb.place(x=0,y=0,relwidth=1,relheight=1)

reg=Label(text="Are You Sure You Want To Logout?",font=("Times New Roman",35),bg="black",fg="gold")
reg.place(x=410,y=250,width=800)

b2 = Button(text="YES", command=main_window, font=("MS Reference Sans Serif", 17),bg="firebrick1", bd=3, relief="raised", activebackground="gold", activeforeground="black")
b2.place(x=505,y=400,width=250)
b3 = Button(text="NO", command=home_win, font=("MS Reference Sans Serif", 17),bg="firebrick1", bd=3, relief="raised", activebackground="gold", activeforeground="black")
b3.place(x=845,y=400,width=250)


rt.mainloop()
