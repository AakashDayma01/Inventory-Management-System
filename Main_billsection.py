from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import string
import sqlite3
import time
import os
import tempfile
import Functions
class Billing_area:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1545x680+-7+135")
        self.root.title("Inventory Management System")
        self.root.resizable(False,False)
        self.f = Functions.function()
        #root.overrideredirect(True)
        self.root.wm_attributes("-topmost",True)
        self.root.focus_force()
        self.cart_list = []
        self.pid = StringVar()
        self.file_print = 0
        self.frame1 = Frame(self.root,bd=4,relief=RIDGE,bg="white",height=670,width=560)
        self.frame1.pack(padx=(0,1050),pady=(0,10))
        self.head1= Label(self.frame1, text="All products",font=("goudy old style",30,"bold"),bg="darkblue",width=580,fg="white",justify=CENTER)
        self.head1.pack(fill=X, pady=(0,580),side=TOP)
        self.search_frame = Frame(self.frame1,bg="white",borderwidth=2,relief=RIDGE,bd=2)
        self.search_frame.place(x=0,y=55,height=110,width=473)

        self.subhead1= Label(self.search_frame, text="Search Product | By Name",font=("goudy old style",18,"bold"),bg="white",width=20,fg="red")
        self.subhead1.place(x=0,y=15)

        self.Search_Name = Label(self.search_frame , text="Product Name" , bg="white",font=("goudy old style",17,"bold") ,)
        self.Search_Name.place(x=0,y=55,width=145,height=50 )
        self.Search_Name_Entry = Entry(self.search_frame,width=20,background="lightyellow", font=("arial",15,"bold"))         
        self.Search_Name_Entry.place(x=145,y=65,width=200)
        self.search_All = Button(self.search_frame , text="Search All" ,command=self.Billsecton_search_all,relief="solid",border=1,highlightthickness=1,padx=20,pady=10, bg="light grey",font=("times new roman"  , 20 ,"bold" ),cursor="hand2").place(x=315 ,y=10, height=40 , width=150)

        self.search_name = Button(self.search_frame , text="Search" ,relief="solid",border=1,highlightthickness=1,padx=20,pady=10, bg="light blue",command=self.Billsection_search,font=("times new roman"  , 20 ,"bold" ),cursor="hand2").place(x=365 ,y=60, height=40 , width=100)
          
        self.Tree_frame = LabelFrame(self.frame1  , font=("times new roman",20,"bold"),bg="white",bd=3 , fg="white")
        self.Tree_frame.place(x=0,y=170,width=475,height=465 )
        self.scrolly = Scrollbar(self.Tree_frame , orient=VERTICAL)
        self.scrollx = Scrollbar(self.Tree_frame , orient=HORIZONTAL)

        self.frameTreaview = ttk.Treeview(self.Tree_frame , columns=("pid" ,"name", "price", "qty", "status") , yscrollcommand=self.scrolly.set , xscrollcommand=self.scrollx.set )
        self.scrolly.pack(side=RIGHT , fill="y")
        self.scrollx.pack(side=BOTTOM , fill="x")
        self.scrollx.config(command=self.frameTreaview.xview )
        self.scrolly.config(command=self.frameTreaview.yview )

        self.frameTreaview.heading("pid", text="P ID" )
        self.frameTreaview.heading("name", text="Name")
        self.frameTreaview.heading("price", text="Price")
        self.frameTreaview.heading("qty", text="QTY")
        self.frameTreaview.heading("status", text="Status")
        self.frameTreaview["show"] = "headings"
        self.frameTreaview.column("pid", width=80 )
        self.frameTreaview.column("name", width=90,anchor="center")
        self.frameTreaview.column("price", width=90,anchor="center")
        self.frameTreaview.column("qty", width=90,anchor="center")
        self.frameTreaview.column("status", width=90,anchor="center")

        self.frameTreaview.pack(fill=BOTH , expand=1)
        self.frameTreaview.bind('<ButtonRelease>',self.Billsection_get_data)

        self.frame2 = Frame(self.root,bd=4,relief=RIDGE,bg="white",height=120,width=450)
        self.frame2.place(x=483 , y=0)
        self.label2 = Label(self.frame2,text="Custumer Detail",font=("goudy old style",20,"bold"),bg="light grey",width=37,height=1,fg="black",justify=CENTER)
        self.label2.pack(fill=X,pady=(2,50))
        self.Custumer_name = Label(self.frame2,text="Name",font=("goudy old style",15,"bold"),bg="white",fg="black",justify=CENTER)
        self.Custumer_name.place(y=50)
        self.Custumer_Name_E = Entry(self.frame2,width=20,background="lightyellow", font=("arial",14,"bold"))         
        self.Custumer_Name_E.place(x=55,y=50,width=200)
        self.Custumer_contact = Label(self.frame2,text="Contact",font=("goudy old style",15,"bold"),bg="white",fg="black",justify=CENTER)
        self.Custumer_contact.place(x=280,y=50)
        self.Custumer_contact_E = ttk.Entry(self.frame2,width=20, font=("arial",14,"bold"))         
        self.Custumer_contact_E.place(x=355,y=50,width=200)
        self.frame3 = LabelFrame(self.root  , font=("times new roman",20,"bold"),bg="white",bd=3 , fg="white")
        self.frame3.place(x=485,y=104,width=570,height=380 )
        self.cart_heading= Label(self.frame3, text="Cart \t \t\t\tTotal Products\t[0]",font=("goudy old style",15,"bold"),bg="lightgrey",width=50,fg="black",justify="left")
        self.cart_heading.place(x=0,y=0)
        self.scrolly = Scrollbar(self.frame3 , orient=VERTICAL)
        self.scrollx = Scrollbar(self.frame3 , orient=HORIZONTAL)
        self.frameTreaview2 = ttk.Treeview(self.frame3 , height=15,columns=("pid" ,"name", "price", "qty") , yscrollcommand=self.scrolly.set , xscrollcommand=self.scrollx.set )
        self.scrolly.pack(side=RIGHT , fill="y")
        self.scrollx.pack(side=BOTTOM , fill="x")
        self.scrollx.config(command=self.frameTreaview2.xview )
        self.scrolly.config(command=self.frameTreaview2.yview )
        self.frameTreaview2.heading("pid", text="P ID" )
        self.frameTreaview2.heading("name", text="Name")
        self.frameTreaview2.heading("price", text="Price")
        self.frameTreaview2.heading("qty", text="QTY")
        self.frameTreaview2["show"] = "headings"
        self.frameTreaview2.column("pid", width=90 )
        self.frameTreaview2.column("name", width=100,anchor="center")
        self.frameTreaview2.column("price", width=100,anchor="center")
        self.frameTreaview2.column("qty", width=100,anchor="center")
        self.frameTreaview2.pack(fill=X ,pady=(20,0) ,expand=1)
        self.frameTreaview2.bind("<ButtonRelease-1>" , self.get_cart_data)
        
        self.frame4 = Frame(self.root,bd=4,relief=RIDGE,bg="white",height=160,width=570)
        self.frame4.place(x=483 , y=480)
        self.Product_name = Label(self.frame4,text="Product Name",font=("goudy old style",18,"bold"),bg="white",fg="black",justify=CENTER)
        self.Product_name.place(x=10,y=10)
        self.p_name_Entry = ttk.Entry(self.frame4,state="readonly",font=("goudy old style",18,"bold"))
        self.p_name_Entry.place(x=10,y=40)
        self.Price_per_qty = Label(self.frame4,text="Price per Qty",font=("goudy old style",18,"bold"),bg="white",fg="black",justify=CENTER)
        self.Price_per_qty.place(x=270,y=10)
        self.price_perqty_Entry = ttk.Entry(self.frame4,font=("goudy old style",18,"bold"),state="readonly")
        self.price_perqty_Entry.place(x=260,y=40,width=160)

        self.Quantity = Label(self.frame4,text="Quantity",font=("goudy old style",18,"bold"),bg="white",fg="black",justify=CENTER)
        self.Quantity.place(x=470,y=10)
        self.Quantity_Entry = Entry(self.frame4,font=("goudy old style",18,"bold"),bg="lightyellow",fg="black")
        self.Quantity_Entry.place(x=425,y=40,width=135)
        self.clear_button = Button(self.frame4 , text="Clear" ,command=self.clear_cart,relief="solid",border=1,highlightthickness=1,padx=20,pady=10, bg="light grey",font=("times new roman"  , 20 ,"bold" ),cursor="hand2").place(x=190 ,y=100, height=40 , width=140)
        self.Add_updatecart_button = Button(self.frame4 , text="Add|Update Cart" ,relief="solid",border=1,highlightthickness=1,padx=20,pady=10, command=self.Add_update_Cart,bg="dark orange",font=("times new roman"  , 20 ,"bold" ),cursor="hand2").place(x=340 ,y=100, height=40 , width=220)
        self.Instock_label = Label(self.frame4,text="In Stock ",font=("goudy old style",18,"bold"),bg="white",fg="black",justify=CENTER)
        self.Instock_label.place(x=10,y=110)

        self.Bill_frame = Frame(self.root,bd=4,relief=RIDGE,bg="white",height=625,width=470)
        self.Bill_frame.place(x=1052,y=0)
        self.Bill_scrollbar = Scrollbar(self.Bill_frame,orient=VERTICAL)
        self.head2= Label(self.Bill_frame, text="Customer Billing Area",font=("goudy old style",27,"bold"),bg="darkorange",width=(23),height=1,fg="black",justify=CENTER)
        self.head2.pack(fill=X, pady=(0,584),side=TOP)
        
        self.Billframe = Label(self.Bill_frame,bd=2,bg="white")
        self.Billframe.place(x=2,y=50,height=470,width=465)
        
        self.billscrollbar = Scrollbar(self.Billframe,orient=VERTICAL)
        self.billtextarea = Text(self.Billframe,font=("goudy old style",15,"bold"),bd=2,state="disabled",bg="lightgrey",fg="black",yscrollcommand=self.billscrollbar.set)
        self.billscrollbar.pack(fill=Y,side=RIGHT)
        self.billscrollbar.config(command=self.billtextarea.yview)
        self.billtextarea.pack(fill=BOTH,expand=1)
        self.Bill_amount_label = Label(self.Bill_frame,text="Billl Amount \n [0]",font=("goudy old style",18,"bold"),bg="darkblue",bd=2,relief=RIDGE,fg="white",justify=CENTER)
        self.Bill_amount_label.place(x=10,y=520)
        self.Discount_label = Label(self.Bill_frame,text="Discount % \n",font=("goudy old style",18,"bold"),bg="dark orange",bd=2,relief=RIDGE,fg="white",justify=CENTER)
        self.Discount_label.place(x=170,y=520,height=62,width=140)
        self.Discount_Entry = Entry(self.Discount_label,textvariable=IntVar(),font=("goudy old style",15,"bold"),bg="lightyellow",fg="black")
        self.Discount_Entry.place(x=12,y=30,width=113)
        self.Bill_netpay_label = Label(self.Bill_frame,text="Net Pay \n [0]",font=("goudy old style",18,"bold"),bg="darkblue",bd=2,relief=RIDGE,fg="white",justify=CENTER)
        self.Bill_netpay_label.place(x=325,y=520,width=130)
        self.print_name_btn = Button(self.Bill_frame , text="Print" ,relief="solid",command=self.Print_File,border=1,highlightthickness=1,padx=20,pady=10, bg="light blue",font=("times new roman"  , 20 ,"bold" ),cursor="hand2").place(x=10 ,y=585, height=45 , width=144)
        self.Clear_All_Btn = Button(self.Bill_frame , text="Clear All" ,relief="solid",border=1,command=self.clear_all,highlightthickness=1,padx=20,pady=10, bg="light green",font=("times new roman"  , 20 ,"bold" ),cursor="hand2").place(x=170 ,y=585, height=45 , width=144)
        self.Genrate_save_bill_btn = Button(self.Bill_frame , text="Generate\n Save Bill" ,relief="solid",command=self.generate_bill,border=1,highlightthickness=1,padx=20,pady=10, bg="light pink",font=("times new roman"  , 16 ,"bold" ),cursor="hand2").place(x=325 ,y=585, height=45 , width=144)
        self.Billsection_show()
   #*******************************Functions*******************************
    def Billsection_show(self):
        self.f.Billsection_show(self.frameTreaview)
    def Billsection_search(self):
        Bill_TUple=(self.root,self.Search_Name_Entry,self.frameTreaview)
        self.f.Billsection_search(Bill_TUple)
    def Billsecton_search_all(self):
        Bill_TUple = (self.root,)
        self.f.Billsecton_search_all(self.frameTreaview,Bill_TUple)
    def Billsection_get_data(self,event = None):
        Bill_TUple = (self.root,self.price_perqty_Entry,self.p_name_Entry,self.Instock_label,self.pid,self.frameTreaview)
        self.f.Billsection_get_data(Bill_TUple)
    def Add_update_Cart(self):
        Bill_TUple = (self.root,self.Quantity_Entry,self.p_name_Entry,self.price_perqty_Entry,self.pid,self.cart_list,self.Discount_Entry,self.frameTreaview2,self.cart_heading,self.Bill_netpay_label,self.Bill_amount_label)
        self.f.Add_updateCart(Bill_TUple)
    def generate_bill(self):
        Bill_tuple= (self.Custumer_Name_E,self.Custumer_contact_E,self.cart_list,self.Discount_Entry,self.Bill_netpay_label,self.Bill_amount_label,self.billtextarea,self.frameTreaview,self.root)
        self.f.generate_bill(Bill_tuple)
    def clear_cart(self):
        Bill_tuple = (self.price_perqty_Entry,self.p_name_Entry,self.pid,self.Quantity_Entry,self.Instock_label,self.Bill_amount_label,self.Bill_netpay_label,self.Discount_Entry)
        self.f.clear_cart(Bill_tuple)
    def clear_all(self):
        Bill_tuple1 = (self.price_perqty_Entry,self.p_name_Entry,self.pid,self.Quantity_Entry,self.Instock_label,self.Bill_amount_label,self.Bill_netpay_label,self.Discount_Entry)
        Bill_TUple2 =(self.root,self.cart_list,self.frameTreaview2,self.cart_heading,self.billtextarea,self.Custumer_Name_E,self.Custumer_contact_E)
        self.f.clear_all(Bill_tuple1,Bill_TUple2)
    def Print_File(self):
        self.f.print_file(self.billtextarea)
    def get_cart_data(self,event = None):
        Bill_tuple =(self.root,self.frameTreaview2,self.price_perqty_Entry,self.p_name_Entry,self.pid,self.Instock_label)
        self.f.get_cart_data(Bill_tuple)

if __name__=="__main__":
    root=Tk()
    obj = Billing_area(root)
    root.mainloop()