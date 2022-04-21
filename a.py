from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as my
db = my.connect(host="localhost",user="root",password="",database="software")
mycursor=db.cursor()
root8= Tk()
root8.title("DISPLAY")
label1 = Label(root8, text="SOFTWARE MANAGEMENT SYSTEM", fg="#06a099", width=35,font=("Sylfaen", 30)).pack()
tree = ttk.Treeview(root8, column=('software_id','software_name','software_price','software_quantity','software_company'))
tree.column('#1',anchor=CENTER)
tree.heading('#1',text="software_id")
tree.column('#2',anchor=CENTER)
tree.heading('#2',text="software_name")
tree.column('#3',anchor=CENTER)
tree.heading('#3',text="software_price")
tree.column('#4',anchor=CENTER)
tree.heading('#4',text="software_quantity")
tree.column('#5',anchor=CENTER)
tree.heading('#5',text="software_company")
try:
    mycursor.execute("select * from ece")
    res = mycursor.fetchall()
    for p in  res:
        tree.insert('','end',values=p)
    tree.pack()
except:
    messagebox.showerror("error","error occured")
root8.mainloop()
