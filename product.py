from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import sqlite3
import Functions
class product:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1335x600+200+135")
        self.root.title("Inventory Management System")
        self.root.resizable(False,False)
        root.overrideredirect(True)
        self.root.focus_force()
        self.f = Functions.function()
        self.product_frame = Frame(self.root,bd=2,relief=RIDGE,bg = "white", )
        self.product_frame.place (x=10,y=10 , width=500,height=530)
        self.tittle = Label(self.product_frame,bg= "black",text="Product Detail",justify="center",font=("goudy old style",18,"bold"),fg = "white" ).pack(fill="x", side="top")
        self.category = Label(self.product_frame , text="Category" , bg="white",font=("goudy old style",20,"bold") ,)
        self.category.place(x=25,y=45,width=125,height=50 )
        self.category_entry = ttk.Combobox(self.product_frame,height=10,cursor="hand2",state="readonly",width=21,values=("Select"), justify=CENTER,font=("arial",15,"bold"))         
        self.category_entry.place(x=180,y=55)
        self.category_entry.current(0)

        self.Supplier = Label(self.product_frame , text="Supplier" , bg="white",font=("goudy old style",20,"bold") ,)
        self.Supplier.place(x=23,y=110,width=125,height=50 )
        self.Supplier_entry = ttk.Combobox(self.product_frame,height=10,cursor="hand2",state="readonly",width=21,values=("Select"), justify=CENTER,font=("arial",15,"bold"))         
        self.Supplier_entry.place(x=180,y=120)
        self.Supplier_entry.current(0)

        self.Name = Label(self.product_frame , text="Name" , bg="white",font=("goudy old style",20,"bold") ,)
        self.Name.place(x=11,y=175,width=125,height=50 )
        self.Name_Entry = Entry(self.product_frame,width=23,background="lightyellow", font=("arial",15,"bold"))         
        self.Name_Entry.place(x=180,y=185)

        self.price = Label(self.product_frame , text="Price" , bg="white",font=("goudy old style",20,"bold") ,)
        self.price.place(x=10,y=245,width=115,height=50 )
        self.price_Entry = Entry(self.product_frame,width=23,background="lightyellow", font=("arial",15,"bold"))         
        self.price_Entry.place(x=180,y=250)

        self.Quantity = Label(self.product_frame , text="QTY" , bg="white",font=("goudy old style",20,"bold") ,)
        self.Quantity.place(x=15,y=310,width=100,height=50 )
        self.Quantity_Entry = Entry(self.product_frame,width=23, font=("arial",15,"bold"),bg="lightyellow")         
        self.Quantity_Entry.place(x=180,y=315)

        self.Status = Label(self.product_frame , text="Status" , bg="white",font=("goudy old style",25,"bold") ,)
        self.Status.place(x=17,y=370,width=125,height=50 )
        self.Status_entry = ttk.Combobox(self.product_frame,height=10,state="readonly",cursor="hand2",width=21,values=("Active", "Inactive"), justify=CENTER,font=("arial",15,"bold"))         
        self.Status_entry.place(x=180,y=380)
        self.Status_entry.current(0)

        btn_add = Button(self.product_frame , text="Save" ,relief="solid",border=1,highlightthickness=1,command=self.product_add,padx=20,pady=10, bg="light blue",font=("times new roman"  , 20 ,"bold" ),cursor="hand2").place(x=25 , y=430 , height=40 , width=100)
        btn_update = Button(self.product_frame , text="Update",padx=20,pady=10,relief="solid",border=1,command=self.product_Update,highlightthickness=2 ,bg="lightgreen",font=("times new roman"  , 20 ,"bold" ),cursor="hand2").place(x=140 , y=430 , height=40 , width=100)
        btn_delete = Button(self.product_frame , text="Delete",command=self.product_delete,relief="solid",border=1,highlightthickness=2 ,padx=20,pady=10, bg="#c59ddf",font=("times new roman"  , 20 ,"bold" ),cursor="hand2").place(x=260 , y=430 , height=40 , width=100)
        btn_cleare = Button(self.product_frame , text="cleare",relief="solid",border=1,highlightthickness=2,command=self.product_clear,padx=20,pady=10, bg="pink",font=("times new roman"  , 20 ,"bold" ),cursor="hand2").place(x=380 , y=430, height=40 , width=100)

        self.frame = LabelFrame(self.root ,text="Search Products",font=("times new roman",20, "bold"),bd=3,width=2100)
        self.frame.pack(padx=(500,0),pady=10)

        self.search_cmb = ttk.Combobox(self.frame,height=10,width=21,state="readonly",cursor="hand2",values=("Select","supplier", "category","name"), justify=CENTER,font=("arial",15,"bold"))         
        self.search_cmb.pack(padx=(20,520),pady=(20,35))
        self.search_cmb.current(0)

        self.search_Entry = Entry(self.frame,width=23,background= "lightyellow", font=("arial",15,"bold"))         
        self.search_Entry.place(x=290,y=(20))
        btn_search = Button(self.frame , text="Search",relief="solid",border=1,highlightthickness=2,padx=20,pady=10, bg="pink",command=self.product_search,font=("times new roman"  , 20 ,"bold" ),cursor="hand2").place(x=590 , y=10, height=45 , width=190)
        self.frame3 = LabelFrame(self.root  , font=("times new roman",20,"bold"),bg="white",bd=3 , fg="white")
        self.frame3.place(x=520,y=150,width=795,height=400 )
        self.scrolly = Scrollbar(self.frame3 , orient=VERTICAL)
        self.scrollx = Scrollbar(self.frame3 , orient=HORIZONTAL)
        self.frameTreaview = ttk.Treeview(self.frame3 , columns=("pid" , "supplier", "category","name", "price", "qty", "status") , yscrollcommand=self.scrolly.set , xscrollcommand=self.scrollx.set )
        self.scrolly.pack(side=RIGHT , fill="y")
        self.scrollx.pack(side=BOTTOM , fill="x")
        self.scrollx.config(command=self.frameTreaview.xview )
        self.scrolly.config(command=self.frameTreaview.yview )
        self.frameTreaview.heading("pid", text="P ID" )
        self.frameTreaview.heading("supplier", text="Supplier")
        self.frameTreaview.heading("category", text="Category")
        self.frameTreaview.heading("name", text="Name")
        self.frameTreaview.heading("price", text="Price")
        self.frameTreaview.heading("qty", text="QTY")
        self.frameTreaview.heading("status", text="Status")
        self.frameTreaview["show"] = "headings"
        self.frameTreaview.column("pid", width=90 )
        self.frameTreaview.column("supplier",  width=100,anchor="center")
        self.frameTreaview.column("category",  width=100,anchor="center")
        self.frameTreaview.column("name", width=100,anchor="center")
        self.frameTreaview.column("price", width=100,anchor="center")
        self.frameTreaview.column("qty", width=100,anchor="center")
        self.frameTreaview.column("status", width=100,anchor="center")
        self.frameTreaview.pack(fill=BOTH , expand=1)
        self.frameTreaview.bind("<ButtonRelease-1>" , self.product_get_data)
        self.Product_show()
        self.fetch_cat_supplier_data()
    def product_add(self):
        Pro_tuple = (self.root,self.Name_Entry,self.category_entry,self.Supplier_entry,self.price_Entry,self.Quantity_Entry,self.Status_entry,self.frameTreaview)
        self.f.product_add(Pro_tuple)
    def Product_show(self):
        self.f.Product_show(self.frameTreaview)
    def product_get_data(self,event =None):
        Pro_tuple = (self.root,self.Name_Entry,self.category_entry,self.Supplier_entry,self.price_Entry,self.Quantity_Entry,self.Status_entry,self.frameTreaview)
        self.f.Product_get_data(Pro_tuple)
    def product_clear(self):
        Pro_tuple = (self.root,self.Name_Entry,self.category_entry,self.Supplier_entry,self.price_Entry,self.Quantity_Entry,self.Status_entry,self.frameTreaview)
        self.f.product_clear(Pro_tuple)
    def product_Update(self):
        Pro_tuple = (self.root,self.Name_Entry,self.category_entry,self.Supplier_entry,self.price_Entry,self.Quantity_Entry,self.Status_entry,self.frameTreaview)
        self.f.product_update(Pro_tuple)
    def product_delete(self):
        Pro_tuple = (self.root,self.Name_Entry,self.category_entry,self.Supplier_entry,self.price_Entry,self.Quantity_Entry,self.Status_entry,self.frameTreaview)
        self.f.product_delete(Pro_tuple)
    def product_search(self):
        Pro_tuple = (self.root,self.search_Entry,self.search_cmb,self.frameTreaview)
        self.f.product_search(Pro_tuple)
    def fetch_cat_supplier_data(self,event =None):
        Pro_tuple = (self.root,self.Supplier_entry,self.category_entry)
        self.f.fetch_cat_supplier_data(Pro_tuple)
if __name__=="__main__":
    root=Tk()
    obj = product(root)
    root.mainloop()