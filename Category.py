from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import sqlite3
from PIL import Image , ImageTk
import Functions
class Categorie:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1335x615+200+135")
        self.root.title("Inventory Management System")
        self.root.resizable(False , False)
        self.root.focus_force()
        self.root.wm_attributes("-topmost",True)
        self.f = Functions.function()
        root.overrideredirect(True)
        ########VAriables########
        self.Cat_var = StringVar()
        self.name_var = StringVar()
        #**************Labels*****************
        self.tittle_frame = Label(self.root , text="Manage Product Categories" , font=("times new roman",30,"bold"),bd=3,relief=RIDGE,bg="black" , fg="white")
        self.tittle_frame.pack(side=TOP,fill=X, padx=10,pady=20)
        self.Name = Label(self.root , text="Enter category Name" , font=("times new roman",20,"bold") ,)
        self.Name.place(x=50,y=100 )
        self.Name_Entry = Entry(self.root,textvariable=self.name_var,font=("arial",15,"bold"),bg="lightyellow")         
        self.Name_Entry.place(x=50,y=150,width=270,height=40)

        btn_add = Button(self.root , text="Save" ,command=self.Cat_add,relief="solid",border=0,padx=20,pady=10, bg="blue",font=("times new roman"  , 20 ,"bold" ),cursor="hand2").place(x=350 , y=150 , height=40 , width=130)
        btn_delete = Button(self.root , text="Delete" ,command=self.Cat_delete,relief="solid",border=0,padx=20,pady=10, bg="red",font=("times new roman"  , 20 ,"bold" ),cursor="hand2").place(x=520 , y=150 , height=40 , width=130)

        self.cat_frame = LabelFrame(self.root  , font=("times new roman",40,"bold"),bg="white",bd=3 , fg="white")
        self.cat_frame.place(x=770,y=100,width=550,height=100 )
        self.scrolly = Scrollbar(self.cat_frame , orient=VERTICAL)
        self.scrollx = Scrollbar(self.cat_frame , orient=HORIZONTAL)
        self.category_table = ttk.Treeview(self.cat_frame , columns=("Cid" , "name") , yscrollcommand=self.scrolly.set , xscrollcommand=self.scrollx.set )
        self.scrolly.pack(side=RIGHT , fill="y")
        self.scrollx.pack(side=BOTTOM , fill="x")
        self.scrollx.config(command=self.category_table.xview )
        self.scrolly.config(command=self.category_table.yview )

        self.category_table.heading("Cid", text="category ID" )
        self.category_table.heading("name", text="Name")
        self.category_table["show"] = "headings"

        self.category_table.column("Cid", width=90 )
        self.category_table.column("name",  width=100,anchor="center")
        self.category_table.pack(fill=BOTH , expand=1)
        self.category_table.bind("<ButtonRelease-1>" , self.Cat_Get_data)
        self.cat_show()

        self.bill_photo = Image.open("pics/p2.jpg")
        self.bill_photo = self.bill_photo.resize((630,330),Image.LANCZOS)
        self.bill_photo = ImageTk.PhotoImage(self.bill_photo)
        self.lbl = Label(self.root,image=self.bill_photo)
        self.lbl.place(x=30,y=220)

        self.bill_photo2 = Image.open("pics/p3.webp")
        self.bill_photo2 = self.bill_photo2.resize((630,330),Image.LANCZOS)
        self.bill_photo2 = ImageTk.PhotoImage(self.bill_photo2)
        self.lbl = Label(self.root,image=self.bill_photo2)
        self.lbl.place(x=680,y=220)



    def Cat_add(self):
        Cattuple = (self.root,self.Name_Entry,self.category_table,self.Cat_var)
        self.f.Categories_add(Cattuple)

    def cat_show(self):
        Cattuple = (self.root,)
        self.f.Categories_show(self.category_table,Cattuple[0])

    def Cat_Get_data(self,event = None):
        Cattuple = (self.root,self.Name_Entry,self.category_table,self.Cat_var)
        self.f.Categories_get_data(Cattuple)

    def Cat_Clear(self):
        Cattuple = (self.root,self.Name_Entry,self.category_table,self.Cat_var)
        self.f.Categories_clear(Cattuple)

    def Cat_delete(self):
        Cattuple = (self.root,self.Name_Entry,self.category_table,self.Cat_var)
        self.f.category_delete(Cattuple)

if __name__=="__main__":
    root=Tk()
    obj = Categorie(root)
    root.mainloop()