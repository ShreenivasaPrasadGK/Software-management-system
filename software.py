from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
from PIL import *
import os
from tkinter import Menu, messagebox
from second import *
import mysql.connector as my
import os
db = my.connect(host="localhost",user="root",password="",database="software")
mycursor=db.cursor()
def valid():
    usre1=username.get()
    pass1=password.get()
    mycursor.execute("select username from login where username=%s and password=%s",(usre1,pass1))
    result=mycursor.fetchone()
    if result==None:
        messagebox.showerror("SOFTWARE","ENTER VALID VALUES")
    else:
        messagebox.showinfo("SOFTWARE","WELCOME"+result[0])
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
# def add1():
    print()
    #ADD.add_command(label="CSE",command=cse) 
# def view():
#     root7=Tk()
#     print()
# def display():
#     root8= Tk()
#     root8.title("MECHANICAL")
#     label1 = Label(root8, text="SOFTWARE MANAGEMENT SYSTEM", fg="#06a099", width=35,font=("Sylfaen", 30)).pack()
#     tree = ttk.Treeview(root8, column=('software_id','software_name','software_price','software_quantity','software_company'))
#     tree.column('#1',anchor=CENTER)
#     tree.heading('#1',text="SOFTWARE_ID")
#     tree.column('#2',anchor=CENTER)
#     tree.heading('#2',text="SOFTWARE_NAME")
#     tree.column('#3',anchor=CENTER)
#     tree.heading('#3',text="SOFTWARE_PRICE")
#     tree.column('#4',anchor=CENTER)
#     tree.heading('#4',text="SOFTWARE_VERSION")
#     tree.column('#5',anchor=CENTER)
#     tree.heading('#5',text="SOFTWARE_COMPANY")
#     try:
#         mycursor.execute("select * from cse")
#         res = mycursor.fetchall()
#         for p in  res:
#             tree.insert('','end',values=p)
#             tree.pack()
#     except:
#         messagebox.showerror("error","error occured")
#     root8.mainloop()
#     root7.mainloop()
    
    
def ec():
    window = tk.Tk() #Creating window
    window.geometry('690x420')
    window.title("ELECTRONICS AND COMM ENGG")
    window.configure(bg="#82E0AA")

    f = "saved_data.pkl"
    if os.path.exists(f): #If file exists then it will read the file
        lst = list(readList(f))
    else:
        lst = []

    window.counter = 0 #counter is initialzed to 0

    def clear():
        #===This function is used to clear all the entry fields===

        prod_id_Entry.config(state='normal')
        prod_id_Entry.delete(0,"end")
        name_Entry.delete(0,"end")
        price_Entry.delete(0,"end")
        quantity_Entry.delete(0,"end")
        company_Entry.delete(0,'end')


    def display():
        root8= Tk()
        root8.title("DISPLAY")
        label1 = Label(root8, text="SOFTWARE MANAGEMENT SYSTEM", fg="#06a099", width=35,font=("Sylfaen", 30)).pack()
        tree = ttk.Treeview(root8, column=('software_id','software_name','software_price','software_quantity','software_company'))
        tree.column('#1',anchor=CENTER)
        tree.heading('#1',text="SOFTWARE_ID")
        tree.column('#2',anchor=CENTER)
        tree.heading('#2',text="SOFTWARE_NAME")
        tree.column('#3',anchor=CENTER)
        tree.heading('#3',text="SOFTWARE_PRICE")
        tree.column('#4',anchor=CENTER)
        tree.heading('#4',text="SOFTWARE_VERSION")
        tree.column('#5',anchor=CENTER)
        tree.heading('#5',text="SOFTWARE_COMPANY")
        try:
            mycursor.execute("select * from ece")
            res = mycursor.fetchall()
            for p in  res:
                tree.insert('','end',values=p)
            tree.pack()
        except:
            messagebox.showerror("error","error occured")
        root8.mainloop()




        

    def addnew2():
        if (prod_id_Entry.get()!=" " and name_Entry.get()!=" " and price_Entry.get()!=" " and quantity_Entry.get()!=" " and
            company_Entry.get()!=" "):#checks if user has left any field empty
                a=prod_id_Entry.get()
                b=name_Entry.get()
                c=price_Entry.get()
                d=quantity_Entry.get()
                e=company_Entry.get()
                #This condition is when there is no same product id present
                mycursor.execute("insert into ece values(%s,%s,%s,%s,%s)",(a,b,c,d,e))
                db.commit()
                print(a,b,c,d,e)
                messagebox.showinfo("Note","Added")
        else:#if user has left any field blank
            messagebox.showwarning("Note","Please fill all the boxes")
        clear()

    def upd():
        c=price_Entry.get()
        d=quantity_Entry.get()
        a=prod_id_Entry.get()
        if c=="" or d=="":
            messagebox.showwarning("Note","Product Id not present")
            clear()
        
        else:
             mycursor.execute("update ece set price=%s,quantity=%s where pdt_id=%s",(c,d,a))
             db.commit()
             messagebox.showinfo("ditails are updated")
        clear()


    def delete1():
        msg = messagebox.askyesno("Note","Are you sure you want to delete".format(prod_id_Entry.get()))
        if msg:#if user clicks yes
            res = delete(lst,prod_id_Entry.get())
            if res:#if Id is present
                messagebox.showinfo("Note","Deleted product with Id {}".format(prod_id_Entry.get()))
                clear()
            else: #if Id is not present
                messagebox.showwarning("Note","Product Id not present")
                clear()
        else:
            clear()


    def save1():
        if (prod_id_Entry.get()!=" " and name_Entry.get()!=" " and price_Entry.get()!=" " and quantity_Entry.get()!=" " and
            company_Entry.get()!=" "):#checks if user has left any field empty
                a=prod_id_Entry.get()
                b=name_Entry.get()
                c=price_Entry.get()
                d=quantity_Entry.get()
                e=company_Entry.get()
                #This condition is when there is no same product id present
                # mycursor.execute("insert into ece values(%s,%s,%s,%s,%s)",(a,b,c,d,e))
                # db.commit()
                # print(a,b,c,d,e)
                messagebox.showinfo("Note","Added")
        else:#if user has left any field blank
            messagebox.showwarning("Note","Please fill all the boxes")
        clear()

    tk.Label(window,text="SOFTWARE MANAGEMENT SYSTEM",font="stencil 20 bold",bg="#82E0AA",fg="brown").grid(row = 0,column=2,pady=(0,15))

    prod_id_Label = tk.Label(window,text="       Software   Id",font="Impact 14",fg="#E67E22",bg="#82E0AA")
    name_Label = tk.Label(window,text="              Software   Name",font="Impact 14",fg="#E67E22",bg="#82E0AA")
    price_Label = tk.Label(window,text="             Software   Price",font="Impact 14",fg="#E67E22",bg="#82E0AA")
    quantity_Label = tk.Label(window,text="                    Software   Version",font="Impact 14",fg="#E67E22",bg="#82E0AA")
    company_Label = tk.Label(window,text = "                    Software   Company",font="Impact 14",fg="#E67E22",bg="#82E0AA")

    prod_id_Entry = tk.Entry(window,borderwidth=3,highlightbackground='#58bbed')
    name_Entry = tk.Entry(window,borderwidth=3,highlightbackground='#58bbed')
    price_Entry = tk.Entry(window,borderwidth=3,highlightbackground='#58bbed')
    quantity_Entry = tk.Entry(window,borderwidth=3,highlightbackground='#58bbed')
    company_Entry = tk.Entry(window,borderwidth=3,highlightbackground='#58bbed')

    prod_id_Label.grid(row=2,column=1)
    name_Label.grid(row = 3,column = 1)
    price_Label.grid(row = 4,column = 1)
    quantity_Label.grid(row=5,column=1)
    company_Label.grid(row=6,column=1)

    prod_id_Entry.grid(row=2,column=2)
    name_Entry.grid(row=3,column=2)
    price_Entry.grid(row=4,column=2)
    quantity_Entry.grid(row=5,column=2)
    company_Entry.grid(row=6,column=2)


    btn_add = tk.Button(window,text="Add",background="lavender",command=addnew2,highlightbackground='#58bbed')
    btn_update = tk.Button(window,text="Update",background="lavender",command=upd,highlightbackground='#58bbed')
    btn_del = tk.Button(window,text="Delete",background="lavender",command=delete1,highlightbackground='#58bbed')
    #btn_save = tk.Button(window,text="Save",background="lavender",command=save1,highlightbackground='#58bbed')
    btn_display = tk.Button(window,text="Display",background="lavender",command=display,highlightbackground='#58bbed')


    btn_add.place(x=75,y=250)
    btn_update.place(x=135,y=250)
    btn_del.place(x=215,y=250)
    #btn_save.place(x=285,y=250)
    btn_display.place(x=285,y=250)
    menubar= Menu(window)
    edit = Menu(menubar, tearoff=0)  
    edit.add_command(label="Undo")  
    menubar.add_cascade(label="EXIT",command=window.quit)
    window.config(menu=menubar)

    window.mainloop()
def civil():
    window = tk.Tk() #Creating window
    window.geometry('690x420')
    window.title("CIVIL ENGG")
    window.configure(bg="snow")

    f = "saved_data.pkl"
    if os.path.exists(f): #If file exists then it will read the file
        lst = list(readList(f))
    else:
        lst = []

    window.counter = 0 #counter is initialzed to 0

    def clear():
        #===This function is used to clear all the entry fields===

        prod_id_Entry.config(state='normal')
        prod_id_Entry.delete(0,"end")
        name_Entry.delete(0,"end")
        price_Entry.delete(0,"end")
        quantity_Entry.delete(0,"end")
        company_Entry.delete(0,'end')


    def display():
        root8= Tk()
        root8.title("DISPLAY")
        label1 = Label(root8, text="SOFTWARE MANAGEMENT SYSTEM", fg="#06a099", width=35,font=("Sylfaen", 30)).pack()
        tree = ttk.Treeview(root8, column=('software_id','software_name','software_price','software_quantity','software_company'))
        tree.column('#1',anchor=CENTER)
        tree.heading('#1',text="SOFTWARE_ID")
        tree.column('#2',anchor=CENTER)
        tree.heading('#2',text="SOFTWARE_NAME")
        tree.column('#3',anchor=CENTER)
        tree.heading('#3',text="SOFTWARE_PRICE")
        tree.column('#4',anchor=CENTER)
        tree.heading('#4',text="SOFTWARE_VERSION")
        tree.column('#5',anchor=CENTER)
        tree.heading('#5',text="SOFTWARE_COMPANY")
        try:
            mycursor.execute("select * from civil")
            res = mycursor.fetchall()
            for p in  res:
                tree.insert('','end',values=p)
            tree.pack()
        except:
            messagebox.showerror("error","error occured")
        root8.mainloop()

    def addnew2():
        if (prod_id_Entry.get()!=" " and name_Entry.get()!=" " and price_Entry.get()!=" " and quantity_Entry.get()!=" " and
            company_Entry.get()!=" "):#checks if user has left any field empty
                a=prod_id_Entry.get()
                b=name_Entry.get()
                c=price_Entry.get()
                d=quantity_Entry.get()
                e=company_Entry.get()
                #This condition is when there is no same product id present
                mycursor.execute("insert into civil values(%s,%s,%s,%s,%s)",(a,b,c,d,e))
                db.commit()
                print(a,b,c,d,e)
                messagebox.showinfo("Note","Added")
        else:#if user has left any field blank
            messagebox.showwarning("Note","Please fill all the boxes")
        clear()
    # def addnew2():
    #     if (prod_id_Entry.get()!=" " and name_Entry.get()!=" " and price_Entry.get()!=" " and quantity_Entry.get()!=" " and
    #             company_Entry.get()):#checks if user has left any field empty
    #         res = addnew(lst,prod_id_Entry.get(),name_Entry.get(),price_Entry.get(),quantity_Entry.get(),
    #                company_Entry.get())
    #         if res: #This condition is when there is no same product id present
    #             messagebox.showinfo("Note","Added")
    #         else: #When there is an existing product id
    #             messagebox.showwarning("Note","Product Id already present")
    #     else:#if user has left any field blank
    #         messagebox.showwarning("Note","Please fill all the boxes")
    #     clear()

    def upd():
        c=price_Entry.get()
        d=quantity_Entry.get()
        a=prod_id_Entry.get()
        if c=="" or d=="":
            messagebox.showwarning("Note","Product Id not present")
            clear()
        
        else:
             mycursor.execute("update civil set price=%s,quantity=%s where pdt_id=%s",(c,d,a))
             db.commit()
             messagebox.showinfo("ditails are updated")
        clear()

    def delete1():
        msg = messagebox.askyesno("Note","Are you sure you want to delete".format(prod_id_Entry.get()))
        if msg:#if user clicks yes
            res=prod_id_Entry.get()
            if res:#if Id is present
                messagebox.showinfo("Note","Deleted product with Id {}".format(prod_id_Entry.get()))
                clear()
            else: #if Id is not present
                messagebox.showwarning("Note","Product Id not present")
                clear()
        else:
            clear()
        sql="DELETE FROM civil WHERE pdt_id='auto134'"
        mycursor.execute(sql)
        db.commit()
        print(mycursor.rowcwnt,"records(s) deleted")
        print(res)
    def save1():
        saveList(f,lst)
        messagebox.showinfo("Note","Data has been saved")


    tk.Label(window,text="SOFTWARE  MANAGEMENT SYSTEM",font="stencil 20 bold",bg="snow",fg='purple').grid(row = 0,column=2,pady=(0,15))
    prod_id_Label = tk.Label(window,text="Software   Id",font="impact 14",bg="snow",fg='maroon')
    name_Label = tk.Label(window,text="       Software   Name",font="impact 14",bg="snow",fg='maroon')
    price_Label = tk.Label(window,text="       Software   Price",font="impact 14",bg="snow",fg='maroon')
    quantity_Label = tk.Label(window,text="          Software  Version",font="impact 14",bg="snow",fg='maroon')
    company_Label = tk.Label(window,text = "          Software   Company",font="impact 14",bg="snow",fg='maroon')

    prod_id_Entry = tk.Entry(window,borderwidth=3,highlightbackground='#58bbed')
    name_Entry = tk.Entry(window,borderwidth=3,highlightbackground='#58bbed')
    price_Entry = tk.Entry(window,borderwidth=3,highlightbackground='#58bbed')
    quantity_Entry = tk.Entry(window,borderwidth=3,highlightbackground='#58bbed')
    company_Entry = tk.Entry(window,borderwidth=3,highlightbackground='#58bbed')

    prod_id_Label.grid(row=2,column=1)
    name_Label.grid(row = 3,column = 1)
    price_Label.grid(row = 4,column = 1)
    quantity_Label.grid(row=5,column=1)
    company_Label.grid(row=6,column=1)

    prod_id_Entry.grid(row=2,column=2)
    name_Entry.grid(row=3,column=2)
    price_Entry.grid(row=4,column=2)
    quantity_Entry.grid(row=5,column=2)
    company_Entry.grid(row=6,column=2)


    btn_add = tk.Button(window,text="Add",command=addnew2,highlightbackground='#58bbed')
    btn_update = tk.Button(window,text="Update",command=upd,highlightbackground='#58bbed')
    btn_del = tk.Button(window,text="Delete",command=delete1,highlightbackground='#58bbed')
   # btn_save = tk.Button(window,text="Save",command=save1,highlightbackground='#58bbed')
    btn_display = tk.Button(window,text="Display",command=display,highlightbackground='#58bbed')


    btn_add.place(x=75,y=250)
    btn_update.place(x=135,y=250)
    btn_del.place(x=215,y=250)
    #btn_save.place(x=285,y=250)
    btn_display.place(x=285,y=250)
    menubar= Menu(window)
    edit = Menu(menubar, tearoff=0)  
    edit.add_command(label="Undo")  
    menubar.add_cascade(label="EXIT",command=window.quit)
    window.config(menu=menubar)

    window.mainloop()
def mech():
    window = tk.Tk() #Creating window
    window.geometry('690x420')
    window.title("MECHANICAL ENGG")
    window.configure(bg="Silver")


    f = "saved_data.pkl"
    if os.path.exists(f): #If file exists then it will read the file
        lst = list(readList(f))
    else:
        lst = []

    window.counter = 0 #counter is initialzed to 0

    def clear():
        #===This function is used to clear all the entry fields===

        prod_id_Entry.config(state='normal')
        prod_id_Entry.delete(0,"end")
        name_Entry.delete(0,"end")
        price_Entry.delete(0,"end")
        quantity_Entry.delete(0,"end")
        company_Entry.delete(0,'end')


    def display():
        root8= Tk()
        root8.title("DISPLAY")
        label1 = Label(root8, text="SOFTWARE MANAGEMENT SYSTEM", fg="#06a099", width=35,font=("Sylfaen", 30)).pack()
        tree = ttk.Treeview(root8, column=('software_id','software_name','software_price','software_quantity','software_company'))
        tree.column('#1',anchor=CENTER)
        tree.heading('#1',text="SOFTWARE_ID")
        tree.column('#2',anchor=CENTER)
        tree.heading('#2',text="SOFTWARE_NAME")
        tree.column('#3',anchor=CENTER)
        tree.heading('#3',text="SOFTWARE_PRICE")
        tree.column('#4',anchor=CENTER)
        tree.heading('#4',text="SOFTWARE_VERSION")
        tree.column('#5',anchor=CENTER)
        tree.heading('#5',text="SOFTWARE_COMPANY")
        try:
            mycursor.execute("select * from ece")
            res = mycursor.fetchall()
            for p in  res:
                tree.insert('','end',values=p)
            tree.pack()
        except:
            messagebox.showerror("error","error occured")
        root8.mainloop()

    # def addnew2():
    #     if (prod_id_Entry.get()!=" " and name_Entry.get()!=" " and price_Entry.get()!=" " and quantity_Entry.get()!=" " and
    #             company_Entry.get()):#checks if user has left any field empty
    #         res = addnew(lst,prod_id_Entry.get(),name_Entry.get(),price_Entry.get(),quantity_Entry.get(),
    #                company_Entry.get())
    #         if res: #This condition is when there is no same product id present
    #             messagebox.showinfo("Note","Added")
    #         else: #When there is an existing product id
    #             messagebox.showwarning("Note","Product Id already present")
    #     else:#if user has left any field blank
    #         messagebox.showwarning("Note","Please fill all the boxes")
    #     clear()
    def addnew2():
        if (prod_id_Entry.get()!=" " and name_Entry.get()!=" " and price_Entry.get()!=" " and quantity_Entry.get()!=" " and
            company_Entry.get()!=" "):#checks if user has left any field empty
                a=prod_id_Entry.get()
                b=name_Entry.get()
                c=price_Entry.get()
                d=quantity_Entry.get()
                e=company_Entry.get()
                #This condition is when there is no same product id present
                mycursor.execute("insert into ece values(%s,%s,%s,%s,%s)",(a,b,c,d,e))
                db.commit()
                print(a,b,c,d,e)
                messagebox.showinfo("Note","Added")
        else:#if user has left any field blank
            messagebox.showwarning("Note","Please fill all the boxes")
        clear()

    def upd():
        c=price_Entry.get()
        d=quantity_Entry.get()
        a=prod_id_Entry.get()
        if c=="" or d=="":
            messagebox.showwarning("Note","Product Id not present")
            clear()
        
        else:
             mycursor.execute("update mechanical set price=%s,quantity=%s where pdt_id=%s",(c,d,a))
             db.commit()
             messagebox.showinfo("ditails are updated")
        clear()

    def delete1():
        msg = messagebox.askyesno("Note","Are you sure you want to delete".format(prod_id_Entry.get()))
        if msg:#if user clicks yes
            res = delete(lst,prod_id_Entry.get())
            if res:#if Id is present
                messagebox.showinfo("Note","Deleted product with Id {}".format(prod_id_Entry.get()))
                clear()
            else: #if Id is not present
                messagebox.showwarning("Note","Product Id not present")
                clear()
        else:
            clear()


    def save1():
        saveList(f,lst)
        messagebox.showinfo("Note","Data has been saved")


    tk.Label(window,text="SOFTWARE MANAGEMENT SYSTEM",font="stencil  20 bold",bg="silver",fg="darkslategray").grid(row = 0,column=2,pady=(0,15))

    prod_id_Label = tk.Label(window,text="Software   Id",font=" Impact 14",bg="silver",fg="darkslateblue")
    name_Label = tk.Label(window,text="Software   Name",font="Impact 14",bg="silver",fg="darkslateblue")
    price_Label = tk.Label(window,text="Software   Price",font="Impact 14",bg="silver",fg="darkslateblue")
    quantity_Label = tk.Label(window,text="Software   Version",font="Impact 14",bg="silver",fg="darkslateblue")
    company_Label = tk.Label(window,text = "Software   Company",font="Impact 14",bg="silver",fg="darkslateblue")

    prod_id_Entry = tk.Entry(window,borderwidth=3,highlightbackground='#58bbed')
    name_Entry = tk.Entry(window,borderwidth=3,highlightbackground='#58bbed')
    price_Entry = tk.Entry(window,borderwidth=3,highlightbackground='#58bbed')
    quantity_Entry = tk.Entry(window,borderwidth=3,highlightbackground='#58bbed')
    company_Entry = tk.Entry(window,borderwidth=3,highlightbackground='#58bbed')

    prod_id_Label.grid(row=2,column=1)
    name_Label.grid(row = 3,column = 1)
    price_Label.grid(row = 4,column = 1)
    quantity_Label.grid(row=5,column=1)
    company_Label.grid(row=6,column=1)

    prod_id_Entry.grid(row=2,column=2)
    name_Entry.grid(row=3,column=2)
    price_Entry.grid(row=4,column=2)
    quantity_Entry.grid(row=5,column=2)
    company_Entry.grid(row=6,column=2)


    btn_add = tk.Button(window,text="Add",command=addnew2,highlightbackground='#58bbed')
    btn_update = tk.Button(window,text="Update",command=upd,highlightbackground='#58bbed')
    btn_del = tk.Button(window,text="Delete",command=delete1,highlightbackground='#58bbed')
    #btn_save = tk.Button(window,text="Save",command=save1,highlightbackground='#58bbed')
    btn_display = tk.Button(window,text="Display",command=display,highlightbackground='#58bbed')


    btn_add.place(x=75,y=250)
    btn_update.place(x=135,y=250)
    btn_del.place(x=215,y=250)
    #btn_save.place(x=285,y=250)
    btn_display.place(x=285,y=250)
    menubar= Menu(window)
    edit = Menu(menubar, tearoff=0)  
    edit.add_command(label="Undo")  
    menubar.add_cascade(label="EXIT",command=window.quit)
    window.config(menu=menubar)

    window.mainloop()

def cse():
    window = tk.Tk() #Creating window
    window.geometry('690x420')
    window.title("COMPUTER SCIENCE AND ENGG")
    window.configure(bg="cornsilk")
    # w, h = window.winfo_screenwidth(), window.winfo_screenheight()
    # window.geometry("%dx%d+0+0" % (w, h))

    f = "saved_data.pkl"
    if os.path.exists(f): #If file exists then it will read the file
        lst = list(readList(f))
    else:
        lst = []

    window.counter = 0 #counter is initialzed to 0

    def clear():
        #===This function is used to clear all the entry fields===

        prod_id_Entry.config(state='normal')
        prod_id_Entry.delete(0,"end")
        name_Entry.delete(0,"end")
        price_Entry.delete(0,"end")
        quantity_Entry.delete(0,"end")
        company_Entry.delete(0,'end')


    def display():
        root8= Tk()
        root8.title("compiuter science")
        label1 = Label(root8, text="SOFTWARE MANAGEMENT SYSTEM", fg="#06a099", width=35,font=("Sylfaen", 30)).pack()
        tree = ttk.Treeview(root8, column=('software_id','software_name','software_price','software_quantity','software_company'))
        tree.column('#1',anchor=CENTER)
        tree.heading('#1',text="SOFTWARE_ID")
        tree.column('#2',anchor=CENTER)
        tree.heading('#2',text="SOFTWARE_NAME")
        tree.column('#3',anchor=CENTER)
        tree.heading('#3',text="SOFTWARE_PRICE")
        tree.column('#4',anchor=CENTER)
        tree.heading('#4',text="SOFTWARE_VERSION")
        tree.column('#5',anchor=CENTER)
        tree.heading('#5',text="SOFTWARE_COMPANY")
        try:
            mycursor.execute("select * from cse")
            res = mycursor.fetchall()
            for p in  res:
                tree.insert('','end',values=p)
            tree.pack()
        except:
            messagebox.showerror("error","error occured")
        root8.mainloop()
    def addnew2():
        if (prod_id_Entry.get()!=" " and name_Entry.get()!=" " and price_Entry.get()!=" " and quantity_Entry.get()!=" " and
            company_Entry.get()!=" "):#checks if user has left any field empty
                a=prod_id_Entry.get()
                b=name_Entry.get()
                c=price_Entry.get()
                d=quantity_Entry.get()
                e=company_Entry.get()
                #This condition is when there is no same product id present
                mycursor.execute("insert into cse values(%s,%s,%s,%s,%s)",(a,b,c,d,e))
                db.commit()
                print(a,b,c,d,e)
                messagebox.showinfo("Note","Added")
        else:#if user has left any field blank
            messagebox.showwarning("Note","Please fill all the boxes")
        clear()

    def upd():
        c=price_Entry.get()
        d=quantity_Entry.get()
        a=prod_id_Entry.get()
        if c=="" or d=="":
            messagebox.showwarning("Note","Product Id not present")
            clear()
        
        else:
             mycursor.execute("update cse set price=%s,quantity=%s where pdt_id=%s",(c,d,a))
             db.commit()
             messagebox.showinfo("ditails are updated")
        clear()

    def delete1():
        msg = messagebox.askyesno("Note","Are you sure you want to delete".format(prod_id_Entry.get()))
        if msg:#if user clicks yes
            res=prod_id_Entry.get()
            if res:#if Id is present
                messagebox.showinfo("Note","Deleted product with Id {}".format(prod_id_Entry.get()))
                clear()
            else: #if Id is not present
                messagebox.showwarning("Note","Product Id not present")
                clear()
        else:
            clear()
        sql="DELETE FROM cse WHERE pdtid='j45'"
        mycursor.execute(sql)
        db.commit()
        print(mycursor.rowcwnt,"records(s) deleted")
        print(res)
    # def delete1():
    #     msg = messagebox.askyesno("Note","Are you sure you want to delete".format(prod_id_Entry.get()))
    #     if msg:#if user clicks yes
    #         res = delete(lst,prod_id_Entry.get())
    #         if res:#if Id is present
    #             messagebox.showinfo("Note","Deleted product with Id {}".format(prod_id_Entry.get()))
    #             clear()
    #         else: #if Id is not present
    #             messagebox.showwarning("Note","Product Id not present")
    #             clear()
    #     else:
            # clear()


    def save1():
        saveList(f,lst)
        messagebox.showinfo("Note","Data has been saved")

    window.title("COMPUTER SCIENCE AND ENGG")
    tk.Label(window,text="SOFTWARE MANAGEMENT SYSTEM",font=("Stencil 20"),fg="midnightblue",bg="cornsilk").grid(row = 0,column=2,pady=(0,15))
    #canvas=window.Canvas()
    prod_id_Label = tk.Label(window,text="  SOFTWARE   ID",font=("Impact 13"),fg="darkOlivegreen")
    #canvas.place(x=10,y=15)
    name_Label = tk.Label(window,text="          SOFTWARE   NAME",font=("Impact 13"),fg="darkolivegreen")
    price_Label = tk.Label(window,text="           SOFTWARE   PRICE",font=("Impact 13"),fg="darkolivegreen")
    quantity_Label = tk.Label(window,text="                   SOFTWARE   VERSION",font=("Impact 13"),fg="darkolivegreen")
    company_Label = tk.Label(window,text = "                     SOFTWARE   COMPANY",font=("Impact 13"),fg="darkolivegreen")

    prod_id_Entry = tk.Entry(window,borderwidth=3,highlightbackground='#58bbed')
    name_Entry = tk.Entry(window,borderwidth=3,highlightbackground='#58bbed')
    price_Entry = tk.Entry(window,borderwidth=3,highlightbackground='#58bbed')
    quantity_Entry = tk.Entry(window,borderwidth=3,highlightbackground='#58bbed')
    company_Entry = tk.Entry(window,borderwidth=3,highlightbackground='#58bbed')

    prod_id_Label.grid(row=2,column=1)
    name_Label.grid(row = 3,column = 1)
    price_Label.grid(row = 4,column = 1)
    quantity_Label.grid(row=5,column=1)
    company_Label.grid(row=6,column=1)

    prod_id_Entry.grid(row=2,column=2)
    name_Entry.grid(row=3,column=2)
    price_Entry.grid(row=4,column=2)
    quantity_Entry.grid(row=5,column=2)
    company_Entry.grid(row=6,column=2)


    btn_add = tk.Button(window,text="Add",command=addnew2,highlightbackground='#58bbed')
    btn_update = tk.Button(window,text="Update",command=upd,highlightbackground='#58bbed')
    btn_del = tk.Button(window,text="Delete",command=delete1,highlightbackground='#58bbed')
    ##btn_save = tk.Button(window,text="Save",command=save1,highlightbackground='#58bbed')
    btn_display = tk.Button(window,text="Display",command=display,highlightbackground='#58bbed')
    btn_display = tk.Button(window,text="display",command=display,highlightbackground='#58bbed')


    btn_add.place(x=85,y=250)
    btn_update.place(x=135,y=250)
    btn_del.place(x=215,y=250)
    #btn_save.place(x=285,y=250)
    btn_display.place(x=285,y=250)
    menubar= Menu(window)
    edit = Menu(menubar, tearoff=0)  
    edit.add_command(label="Undo")  
    menubar.add_cascade(label="EXIT",command=window.quit)
    window.config(menu=menubar)
    window.mainloop()

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
    # Button(root,text="ADD",bg="blue",command=add1,font=('ArialBlack 15')).place(x=150,y=100)
    # Button(root,text="VIEW",bg="blue",command=view,font=('ArialBlack 15')).place(x=250,y=100)
    menubar = Menu(root)  
    Department= Menu(menubar, tearoff=0)  
    Department.add_command(label="CSE",command=cse)  
    Department.add_command(label="MECHANICAL",comman=mech)  
    Department.add_command(label="CIVIL",command=civil)  
    Department.add_command(label="ELECTTRONIC COMM",command=ec)    
    #menubar.add_cascade(label="LOGIN",command=login)
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
# Button(root1,text="ADD",bg="blue",command=add1,font=('ArialBlack 15')).place(x=150,y=40)
# Button(root1,text="VIEW",bg="blue",command=view,font=('ArialBlack 15')).place(x=250,y=40)
root1.mainloop()
