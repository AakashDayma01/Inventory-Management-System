from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import sqlite3
from tkcalendar import Calendar
import string
from datetime import datetime
import Functions
class page2:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1335x615+200+135")
        self.root.title("Inventory Management System")
        self.root.resizable(False,False)
        self.f = Functions.function()
        root.overrideredirect(True)
        self.root.wm_attributes("-topmost",True)
        self.lbl = None
        self.lbl1 = None
        self.root.focus_force()
        self.frame = LabelFrame(self.root ,text="Search Employee",font=("times new roman",20, "bold"),bd=3,height=90,width=800)
        self.frame.pack(padx=100,pady=10)
        self.searchby = ttk.Combobox(self.frame,values=("Select","Email","name","contact"),state="readonly",justify=CENTER,height=10,width=20,font=("arial",15,"bold"))         
        self.searchby.place(x=20,y=5)
        self.searchby.current(0)
        self.frame2 = Label(self.root , text="Employee Details" , font=("times new roman",20,"bold"),bg="black" , fg="white")
        self.frame2.place(x=30,y=110,width=1275,height=40 )
        self.search1 = ttk.Entry(self.frame,font=("arial",15,"bold"))         
        self.search1.place(x=300,y=5)
        btn_Search = Button(self.frame , text="Search" ,command=self.Search_data,relief="solid",border=1,padx=20,pady=10, bg="dark grey",font=("times new roman"  , 20 ,"bold" ),cursor="hand2").place(x=570 , y=-6 , height=50 , width=190)
        self.Emp_no = Label(self.root , text="Emp No." , font=("times new roman",20,"bold") ,)
        self.Emp_no.place(x=32,y=170,width=125,height=50 )
        self.Emp_Entry = ttk.Entry(self.root,state="readonly",font=("arial",15,"bold"))         
        self.Emp_Entry.place(x=180,y=175)
        self.gender = Label(self.root , text="Gender" , font=("times new roman",20,"bold") ,)
        self.gender.place(x=425,y=165,width=125,height=60 )
        self.gender_entry = ttk.Combobox(self.root,height=10,width=20,values=("Select","Male" , "Female"),state="readonly",justify=CENTER,font=("arial",15,"bold"))         
        self.gender_entry.place(x=590,y=170)
        self.gender_entry.current(0)
        self.dob= Label(self.root , text="D.O.B."  ,font=("times new roman",20,"bold"))
        self.dob.place(x=425,y=220,width=125,height=50 )
        self.dob_Entry = ttk.Entry(self.root,font=("arial",15,"bold"),state="readonly",)         
        self.dob_Entry.place(x=590,y=230,width=245)
        self.dob_Entry.bind("<Button-1>", self.Show_caleder_dob)
        self.password= Label(self.root , text="Password" , font=("times new roman",20,"bold") ,)
        self.password.place(x=440,y=275,width=125,height=50 )
        self.password_Entry = ttk.Entry(self.root,font=("arial",15,"bold"))         
        self.password_Entry.place(x=590,y=285,width=245)

        self.name = Label(self.root , text="Name" , font=("times new roman",20,"bold") ,)
        self.name.place(x=15,y=220,width=125,height=50 )
        self.name_Entry = ttk.Entry(self.root,font=("arial",15,"bold"))         
        self.name_Entry.place(x=180,y=230)
        self.email = Label(self.root , text="Email" , font=("times new roman",20,"bold") ,)
        self.email.place(x=15,y=275,width=125,height=50 )
        self.email_Entry = ttk.Entry(self.root,textvariable=StringVar(),font=("arial",15,"bold"))         
        self.email_Entry.place(x=180,y=285)

        self.contact = Label(self.root , text="Contact No." , font=("times new roman",20,"bold") ,)
        self.contact.place(x=870,y=155,width=140,height=50 )
        self.contact_Entry = ttk.Entry(self.root,font=("arial",15,"bold"))         
        self.contact_Entry.place(x=1050,y=160, width=240)
        self.doj = Label(self.root , text="D.O.J." , font=("times new roman",20,"bold") ,)
        self.doj.place(x=850,y=220,width=125,height=50 )
        self.doj_Entry = ttk.Entry(self.root,state="readonly",font=("arial",15,"bold"))         
        self.doj_Entry.place(x=1050,y=220 ,width=240)
        self.doj_Entry.bind("<Button-1>", self.Show_caleder_doj)
        self.usert_type = Label(self.root , text="User Type" , font=("times new roman",20,"bold") ,)
        self.usert_type.place(x=870,y=265,width=125,height=60 )
        self.usert_type_cmb = ttk.Combobox(self.root,height=10,width=20,values=("Admin","Employee"),justify=CENTER,state="readonly",font=("arial",15,"bold"))         
        self.usert_type_cmb.place(x=1050,y=280)
        self.usert_type_cmb.current(0)

        self.Address = Label(self.root , text="Address" , font=("times new roman",20,"bold") ,)
        self.Address.place(x=26,y=330,width=125,height=50 )
        self.Address_Entry = Text(self.root,font=("arial",15,"bold"))         
        self.Address_Entry.place(x=180,y=340 ,width=300 ,height=70)
        self.Salary= Label(self.root , text="Salary" , font=("times new roman",20,"bold") ,)
        self.Salary.place(x=480,y=320,width=125,height=50 )
        self.Salary_Entry = ttk.Entry(self.root,font=("arial",15,"bold"))         
        self.Salary_Entry.place(x=630,y=330,width=245)

        btn_add = Button(self.root , text="Save" ,relief="solid",border=0,padx=20,pady=10, borderwidth=1,bg="light blue",command=self.ad_data,font=("times new roman"  , 20 ,"bold" ),cursor="hand2").place(x=490 , y=370 , height=40 , width=170)
        btn_update = Button(self.root , text="Update" ,command=self.Update_data,relief="solid",borderwidth=1,padx=20,pady=10, bg="light green",font=("times new roman"  , 20 ,"bold" ),cursor="hand2").place(x=710 , y=370 , height=40 , width=170)
        btn_delete = Button(self.root , text="Delete" ,command=self.Delete,relief="solid",border=0,padx=20,borderwidth=1,pady=10, bg="light grey",font=("times new roman"  , 20 ,"bold" ),cursor="hand2").place(x=930 , y=370 , height=40 , width=170)
        btn_cleare = Button(self.root , text="cleare" ,command=self.clear_data,relief="solid",border=0,padx=20,borderwidth=1,pady=10, bg="pink",font=("times new roman"  , 20 ,"bold" ),cursor="hand2").place(x=1150 , y=370, height=40 , width=170)

        self.frame3 = LabelFrame(self.root  , font=("times new roman",20,"bold"),bg="white",bd=3 , fg="white")
        self.frame3.place(x=20,y=420,width=1285,height=140 )
        self.scrolly = Scrollbar(self.frame3 , orient=VERTICAL)
        self.scrollx = Scrollbar(self.frame3 , orient=HORIZONTAL)
        self.frameTreaview = ttk.Treeview(self.frame3 , columns=("eid" , "name", "email","gender", "contact", "dob", "doj","pass" , "utype","address" , "salary") , yscrollcommand=self.scrolly.set , xscrollcommand=self.scrollx.set )
        self.scrolly.pack(side=RIGHT , fill="y")
        self.scrollx.pack(side=BOTTOM , fill="x")
        self.scrollx.config(command=self.frameTreaview.xview )
        self.scrolly.config(command=self.frameTreaview.yview )

        self.frameTreaview.heading("eid", text="EMP ID" )
        self.frameTreaview.heading("name", text="Name")
        self.frameTreaview.heading("email", text="Email")
        self.frameTreaview.heading("gender", text="Gender")
        self.frameTreaview.heading("contact", text="Contact")
        self.frameTreaview.heading("dob", text="D.O.B")
        self.frameTreaview.heading("doj", text="D.O.J")
        self.frameTreaview.heading("pass", text="Password")
        self.frameTreaview.heading("utype", text="User Type")
        self.frameTreaview.heading("address", text="Address")
        self.frameTreaview.heading("salary", text="Salary")
        self.frameTreaview["show"] = "headings"
        self.frameTreaview.column("eid", width=90 )
        self.frameTreaview.column("name",  width=100)
        self.frameTreaview.column("email",  width=100)
        self.frameTreaview.column("gender", width=100)
        self.frameTreaview.column("contact", width=100)
        self.frameTreaview.column("dob", width=100)
        self.frameTreaview.column("doj", width=100)
        self.frameTreaview.column("pass", width=100)
        self.frameTreaview.column("utype", width=100)
        self.frameTreaview.column("address", width=100)
        self.frameTreaview.column("salary", width=100)
        self.frameTreaview.pack(fill=BOTH , expand=1)
        self.frameTreaview.bind("<ButtonRelease-1>" , self.Get_Data)
        self.generateeId()
        self.show_data(self.frameTreaview)
    def ad_data(self):
        mytuple = (self.root,self.Emp_Entry,self.name_Entry,self.email_Entry,self.gender_entry,self.contact_Entry,self.dob_Entry,self.doj_Entry,self.password_Entry,self.usert_type_cmb,self.Address_Entry,self.Salary_Entry ,self.frameTreaview)
        self.f.add(mytuple)
    def clear_data(self):
        mytuple=(self.root,self.Emp_Entry,self.name_Entry,self.email_Entry,self.gender_entry,self.contact_Entry,self.dob_Entry,self.doj_Entry,self.password_Entry,self.usert_type_cmb,self.Address_Entry, self.Salary_Entry )
        self.f.clear(mytuple)
    def show_data(self,frameTreaview):
        self.f.show(self.frameTreaview,self.root)
    def generateeId(self):
        Eid_tuple = (self.Emp_Entry,)
        self.f.generateeid(Eid_tuple)                                         
    def Get_Data(self,event = None):
        mytuple = (self.root,self.Emp_Entry,self.name_Entry,self.email_Entry,self.gender_entry,self.contact_Entry,self.dob_Entry,self.doj_Entry,self.password_Entry,self.usert_type_cmb,self.Address_Entry,self.Salary_Entry ,self.frameTreaview)
        self.f.get_data(mytuple)
    def Update_data(self):
        mytuple = (self.root,self.Emp_Entry,self.name_Entry,self.email_Entry,self.gender_entry,self.contact_Entry,self.dob_Entry,self.doj_Entry,self.password_Entry,self.usert_type_cmb,self.Address_Entry,self.Salary_Entry ,self.frameTreaview)
        self.f.update(mytuple)
    def Delete(self):
        mytuple = (self.root,self.Emp_Entry,self.name_Entry,self.email_Entry,self.gender_entry,self.contact_Entry,self.dob_Entry,self.doj_Entry,self.password_Entry,self.usert_type_cmb,self.Address_Entry,self.Salary_Entry ,self.frameTreaview)
        self.f.delete(mytuple)
    def Search_data(self):
        mytuple = (self.root,self.search1,self.searchby,self.frameTreaview)
        self.f.search(mytuple)
    def Show_caleder_dob(self,event = None):
        MyTuple = (self.dob_Entry,self.root)
        self.f.show_calendar(MyTuple,self.lbl)
    def Show_caleder_doj(self,event = None):
        MyTuple = (self.doj_Entry,self.root)
        self.f.show_calendar_doj(MyTuple,self.lbl1)
if __name__=="__main__":
    root=Tk()
    obj = page2(root)
    root.mainloop()
