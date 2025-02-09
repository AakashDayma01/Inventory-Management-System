from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import sqlite3
import Functions
class SupplyreClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1335x615+200+135")
        self.root.title("Inventory Management System")
        self.root.focus_force()
        self.f = Functions.function()
        root.overrideredirect(True)
        lbl_search = Label(self.root,text="Invoice no ",height=1,font=("times new roman",25,"bold"))         
        lbl_search.place(x=770,y=70)
        self.Search_Entry = ttk.Entry(self.root,font=("arial",15,"bold"))         
        self.Search_Entry.place(x=930,y=80)
        self.frame2 = Label(self.root , text="Supplier Details" , font=("times new roman",20,"bold"),bg="black" , fg="white")
        self.frame2.place(x=30,y=18,width=1275,height=45 )
        btn_Search = Button(self.root , text="Search" ,command=self.Sup_Search,relief="solid",border=1,padx=20,pady=10, bg="green",font=("times new roman"  , 20 ,"bold" ),cursor="hand2").place(x=1180 , y=70 , height=40 , width=140)
        self.Sup_no = Label(self.root , text="Invoice No." , font=("times new roman",20,"bold") ,)
        self.Sup_no.place(x=32,y=70,width=135,height=50 )
        self.Sup_Entry = ttk.Entry(self.root,font=("arial",15,"bold"))         
        self.Sup_Entry.place(x=180,y=75)
       
        self.name = Label(self.root , text="Name" , font=("times new roman",20,"bold") ,)
        self.name.place(x=7,y=125,width=125,height=50 )
        self.name_Entry = ttk.Entry(self.root,font=("arial",15,"bold"))         
        self.name_Entry.place(x=180,y=130)
        self.Contact = Label(self.root , text="Contact" , font=("times new roman",20,"bold") ,)
        self.Contact.place(x=10,y=175,width=135,height=50 )
        self.Contact_Entry = ttk.Entry(self.root,font=("arial",15,"bold"))         
        self.Contact_Entry.place(x=180,y=185)

        self.Desc = Label(self.root , text="Description" , font=("times new roman",20,"bold") ,)
        self.Desc.place(x=26,y=230,width=135,height=50 )
        self.DEsc_Entry = Text(self.root,font=("arial",15,"bold"))         
        self.DEsc_Entry.place(x=180,y=240 ,width=400 ,height=100)
        btn_add = Button(self.root , text="Save" ,relief="solid",border=1,padx=20,pady=10, bg="blue",command=self.Sup_Add,font=("times new roman"  , 20 ,"bold" ),cursor="hand2").place(x=100 , y=380 , height=40 , width=130)
        btn_update = Button(self.root , text="Update" ,command=self.Sup_Update,relief="solid",border=1,padx=20,pady=10, bg="green",font=("times new roman"  , 20 ,"bold" ),cursor="hand2").place(x=260 , y=380 , height=40 , width=130)
        btn_delete = Button(self.root , text="Delete" ,command=self.Sup_Delete,relief="solid",border=1,padx=20,pady=10, bg="red",font=("times new roman"  , 20 ,"bold" ),cursor="hand2").place(x=420 , y=380 , height=40 , width=130)
        btn_cleare = Button(self.root , text="cleare" ,command=self.Sup_Clear,relief="solid",border=1,padx=20,pady=10, bg="pink",font=("times new roman"  , 20 ,"bold" ),cursor="hand2").place(x=585 , y=380, height=40 , width=130)
        self.frame3 = LabelFrame(self.root  , font=("times new roman",40,"bold"),bg="white",bd=3 , fg="white")
        self.frame3.place(x=770,y=120,width=550,height=440 )
        self.scrolly = Scrollbar(self.frame3 , orient=VERTICAL)
        self.scrollx = Scrollbar(self.frame3 , orient=HORIZONTAL)
        self.Supplier_Table = ttk.Treeview(self.frame3 , columns=("Invoice" , "name", "contact","description") , yscrollcommand=self.scrolly.set , xscrollcommand=self.scrollx.set )
        self.scrolly.pack(side=RIGHT , fill="y")
        self.scrollx.pack(side=BOTTOM , fill="x")
        self.scrollx.config(command=self.Supplier_Table.xview )
        self.scrolly.config(command=self.Supplier_Table.yview )

        self.Supplier_Table.heading("Invoice", text="Invoice No." )
        self.Supplier_Table.heading("name", text="Name")
        self.Supplier_Table.heading("contact", text="Contact")
        self.Supplier_Table.heading("description", text="Description")
        self.Supplier_Table["show"] = "headings"

        self.Supplier_Table.column("Invoice", width=90 )
        self.Supplier_Table.column("name",  width=100)
        self.Supplier_Table.column("contact",  width=100)
        self.Supplier_Table.column("description", width=100)
        self.Supplier_Table.pack(fill=BOTH , expand=1)
        self.Supplier_Table.bind("<ButtonRelease-1>" , self.Sup_Get_data)
        self.Sup_show(self.Supplier_Table)
        self.Sup_generateInvoice()
    def Sup_Add(self):
        mytuple = (self.root,self.Sup_Entry,self.name_Entry,self.Contact_Entry,self.DEsc_Entry,self.Supplier_Table,self.Search_Entry)
        self.f.Suplier_add(mytuple)

    def Sup_show(self,Supplier_Table):
        mytuple = (self.root,)
        self.f.Suplier_show(self.Supplier_Table,mytuple[0])

    def Sup_Get_data(self,event = None):
        mytuple = (self.root,self.Sup_Entry,self.name_Entry,self.Contact_Entry,self.DEsc_Entry,self.Supplier_Table,self.Search_Entry)
        self.f.Suplier_get_data(mytuple)

    def Sup_Update(self):
        mytuple = (self.root,self.Sup_Entry,self.name_Entry,self.Contact_Entry,self.DEsc_Entry,self.Supplier_Table,self.Search_Entry)
        self.f.Suplier_Update(mytuple)

    def Sup_Clear(self):
        MYtuple = (self.root,self.Sup_Entry,self.name_Entry,self.Contact_Entry,self.DEsc_Entry,self.Supplier_Table,self.Search_Entry)
        self.f.Suplier_Clears(MYtuple)

    def Sup_Delete(self):
        MYtuple = (self.root,self.Sup_Entry,self.name_Entry,self.Contact_Entry,self.DEsc_Entry,self.Supplier_Table,self.Search_Entry)
        self.f.Suplier_Delete(MYtuple)

    def Sup_generateInvoice(self):
        self.f.Suplir_generateInvoice(self.Sup_Entry)

    def Sup_Search(self):
        MYtuple = (self.root,self.Supplier_Table,self.Search_Entry)
        self.f.suplier_search(MYtuple)

if __name__=="__main__":
    root=Tk()
    obj = SupplyreClass(root)
    root.mainloop()