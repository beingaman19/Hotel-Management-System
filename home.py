from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk #pip install Pillow
def booking_window():
    rt.destroy()
    import booking




def logout_window():
    rt.destroy()
    import logout
rt=Tk()
rt.title("Reception Lounge")
rt.geometry("1334x699+0+0")
bg=ImageTk.PhotoImage(file="H6.jpg")
bglb=Label(rt,image=bg)
bglb.place(x=0,y=0,relwidth=1,relheight=1)

reg=Label(text="Welcome to Hotel SunShine",font=("Forte",35),bg="red",fg="white")
reg.place(x=10,y=20,width=600)

reg2 = Label(text="Customer Booking",font=("Pristina",30), bg="gold", fg="black")
reg2.place(x=800, y=120,width=400)

b2=Button(text="Booking",command=booking_window,font=("MS Reference Sans Serif",17),fg="gold",bg="black",borderwidth=3,relief="raised",activebackground="gold",activeforeground="black")
b2.place(x=800,y=210,width=150)

b7 = Button(text="Logout", command=logout_window, font=("MS Reference Sans Serif",17), bg="black",fg="gold", borderwidth=3, relief="raised", activebackground="gold", activeforeground="black")
b7.place(x=800,y=280,width=150)

rt.mainloop()
