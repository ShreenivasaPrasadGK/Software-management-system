from tkinter import *
from PIL import ImageTk,Image
from PIL import *
import mysql.connector as my
import os
db = my.connect(host="localhost",user="root",password="",database="software")
mycursor=db.cursor()
def valid():
    usre1=username.get()
    pass1=password.get()
    mycursor.execute("insert into login values(%s,%s)",(usre1,pass1))
    db.commit()
    if(usre1=="" and pass1==""):
        Label(login_screen,text=":Fill the filleds:",fg="red").pack()
    elif(usre1==""):
        Label(login_screen,text=":Enter correct username",fg="red").pack()
    elif(pass1==""):
        Label(login_screen,text=":Enter correct password",fg="red").pack()
    else:
        Label(login_screen,text="successfull",fg="green").pack()
        main()

     
    

def login():
    global login_screen ,password,username
    login_screen=Tk()
    #login_screen.configure(bg="lightblue")
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="LOGIN",font=('arial  11 bold')).place(x=400,y=42)
    Label(login_screen, text="Username").pack()
    username=Entry(login_screen)
    username.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password").pack()
    password=Entry(login_screen, show= '*')
    password.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", fg="white",bg="black",width=10, height=1,command=valid).pack()
    login_screen.mainloop()

def ec():
    import ecmain
def civil():
    import cvmain
def mech():
    import mechmain
def cse():
    import csmain
# def login():
#     global login_screen ,password,username
#     login_screen=Tk()
#     login_screen.title("LOGIN")
#     login_screen.geometry("300x250")
    
#     Label(login_screen, text="LOGIN",font=('arial  11 bold')).pack()
#     Label(login_screen, text="").pack()
#     Label(login_screen, text="Username").pack()
#     username=Entry(login_screen)
#     username.pack()
#     Label(login_screen, text="").pack()
#     Label(login_screen, text="Password").pack()
#     password=Entry(login_screen, show= '*')
#     password.pack()
#     Label(login_screen, text="").pack()
#     Button(login_screen, text="Login",fg="white",bg="black",width=10, height=1,command=valid).pack()
#     login_screen.mainloop()
def main():
    root=Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.title("SOFTWARE TOOL MANGEMENT")
    root.configure(bg="lightskyblue")
    Label(root,text="SOFTWARE MANAGEMENT SYSTEM",font=('Algerian 25 bold'),fg="firebrick",bg="lightskyblue").place(x=400,y=42)
    #----------------------------------------*image open*-----------------------------------#
    # canvas=Canvas(root,width=300,height=100)
    # imag=ImageTk.PhotoImage(Image.open("test_img.png"))
    # # canvas.create_image(0,0,anchor=NW,image=imag)
    # # root.grid()
    #-----------------------------------------*menu*----------------------------------------#
    menubar = Menu(root)  
    Department= Menu(menubar, tearoff=0)  
    Department.add_command(label="CSE",command=cse)  
    Department.add_command(label="MECHANICAL",comman=mech)  
    Department.add_command(label="CIVIL",command=civil)  
    Department.add_command(label="ELECTTRONIC COMM",command=ec)    
    menubar.add_cascade(label="LOGIN",command=login)
    menubar.add_cascade(label="DEPARTMENT", menu=Department)  
    edit = Menu(menubar, tearoff=0)  
    edit.add_command(label="Undo")  
    menubar.add_cascade(label="EXIT",command=root.quit)
    root.config(menu=menubar)  
    root.mainloop()
root1=Tk()
root1.title("HOME")
w, h = root1.winfo_screenwidth(), root1.winfo_screenheight()
root1.geometry("%dx%d+0+0" % (w, h))
#root.configure(bg="skyblue")
canvas1=Canvas(root1,width=300,height=100)
image1=ImageTk.PhotoImage(Image.open("C:\\Users\\Srinivas\\Downloads\\ProductManagementGUI-master\\test_img.png"))
canvas1.create_image(0,0,anchor=NW,image=image1)
canvas1.place(x=0,y=120,width=8000,height=10000)
Button(root1,text="LOGIN",bg="blue",command=login,font=('ArialBlack 15')).place(x=30,y=40)
root1.mainloop()
