from tkinter import *
from Employee import page2
import time
import os
import sqlite3
from Category import Categorie
from Sales import Sales
from suplyre import SupplyreClass
from product import product
from datetime import datetime
from PIL import Image , ImageTk
from Main_billsection import Billing_area
class page1:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.page_window = None
        self.page1_window = None
        self.page2_window = None
        self.page3_window = None
        self.page4_window = None
        self.page5_window = None
        self.page6_window = None
        self.root.state('zoomed')
        self.root.configure(background = "white")
        self.root.resizable(False,False)
        tittlt = Label(self.root , text="Inventory Management System " , font=("times new roman",40, "bold"),bg="#010c48" ,anchor="w" , padx=20, fg="white")
        tittlt.place(x=0, y=0,relwidth=1,height=70 )
        btn_logout = Button(self.root , text="Logout" , bg="skyblue",font=("times new roman"  , 20 ,"bold" ),cursor="hand2").place(x=1200 , y=10 , height=50 , width=150)
        btn_logout = Button(self.root , text="Close" ,fg="black", bg="#FFA07A",font=("times new roman"  , 20 ,"bold" ),command=self.Close,cursor="hand2").place(x=1370 , y=10 , height=50 , width=150)
        self.tittlt2 = Label(self.root , text=f"Welcome to Inventory Management System \t\t   Date DD/YY/MM  \t\t  Time HH:MM:SS" , font=("times new roman",20, "bold"),bg="black" ,anchor="w" , padx=30, fg="white")
        self.tittlt2.place(y=70,relwidth=1,height=40 )
        self.Sideframe = Label(self.root , bd=2 , relief=RIDGE)
        self.Sideframe.place(x = 0 ,y= 111 ,width=200,height=610 )
        self.bill_photo = Image.open("pics/p1.jpg")
        self.bill_photo = self.bill_photo.resize((185,185),Image.LANCZOS)
        self.bill_photo = ImageTk.PhotoImage(self.bill_photo)
        self.lbl = Label(self.Sideframe,image=self.bill_photo)
        self.lbl.place(x=4,y=5)        
        self.MAin_billsection_btn = Button(self.Sideframe , text=" Add Employee" , command=self.employee2,bg="lightgrey",font=("times new roman" , 20 ,"bold" ),cursor="hand2")
        self.MAin_billsection_btn.place(x=3 , y=195  ,height=60 , width=190)
        self.Employee_Btn = Button(self.Sideframe , text="Billing Section" , command=self.Bill_Area,bg="lightpink",font=("times new roman" , 20 ,"bold" ),cursor="hand2").place(x=3 , y=265 ,height=60 , width=190)
        self.Sales_Btn = Button(self.Sideframe , text="Sales Section" , command=self.Sales,bg="light blue",font=("times new roman" , 20 ,"bold" ),cursor="hand2").place(x=3 , y=335 ,height=60 , width=190)
        self.Categorie_Btn = Button(self.Sideframe , text="Product Category" , command=self.category,bg="#FFA07A",font=("times new roman" , 17 ,"bold" ),cursor="hand2").place(x=3 , y=405 ,height=60 , width=190)
        self.Suplier_btn = Button(self.Sideframe , text="Add Suplier" , command=self.Suplier,bg="#E6E6FA",font=("times new roman" , 20 ,"bold" ),cursor="hand2").place(x=3 , y=475 ,height=60 , width=190)
        self.Product_btn = Button(self.Sideframe , text="Add Product" , command=self.product,bg="#ffffe0",font=("times new roman" , 20 ,"bold" ),cursor="hand2").place(x=3 , y=545 ,height=60 , width=190)
        self.Total_Emp_lbl = Label(self.root , text="Total Employee\n[ ]",borderwidth=2, font=("times new roman",20, "bold"),bg="lightgreen" , padx=20)
        self.Total_Emp_lbl.place(x=280 , y=135  ,height=100 , width=300)
        self.Total_sales_lbl = Label(self.root , text="Total Sales\n[ ]" , font=("times new roman",20, "bold"),bg="lightgrey" , padx=20)
        self.Total_sales_lbl.place(x=675 , y=135 , height=100 , width=300)
        self.Totoal_ptoduct = Label(self.root , text="Total Products\n[ ]",borderwidth=2, font=("times new roman",20, "bold"), bg="lightblue" , padx=20)
        self.Totoal_ptoduct.place(x=1055 , y=135, height=100 , width=300)
        self.Total_suplier = Label(self.root , text="Total supliers\n[ ]",borderwidth=2, font=("times new roman",20, "bold"),bg="lightpink" , padx=20)
        self.Total_suplier.place(x=280 , y=290, height=100 , width=300)
        self.Total_Categories = Label(self.root , text="Total Categories\n[ ]",borderwidth=2, font=("times new roman",20, "bold"),bg="skyblue", padx=20)
        self.Total_Categories.place(x=675 , y=290, height=100 , width=300)
        tittlt3 = Label(self.root , text="Inventory Management System | Developed by Aakash \nFor any technical issue contact 6267xxxx74" , font=("times new roman",20),bg="black" , fg="white")
        tittlt3.place(x=0, y=735,relwidth=1,height=80 )
        
        self.Counter_photo2 = Image.open("pics/Screenshot.png")
        self.Counter_photo2 = self.Counter_photo2.resize((600,330),Image.LANCZOS)
        self.Counter_photo2 = ImageTk.PhotoImage(self.Counter_photo2)
        self.lbl = Label(self.root,image=self.Counter_photo2)
        self.lbl.place(x=375,y=400)   
        
        self.Counter_photo = Image.open("pics/All_inventory2.jpg")
        self.Counter_photo = self.Counter_photo.resize((550,460),Image.LANCZOS)
        self.Counter_photo = ImageTk.PhotoImage(self.Counter_photo)
        self.lbl = Label(self.root,image=self.Counter_photo)
        self.lbl.place(x=980,y=245)     
        self.update_time()

    def Close(self):
        if self.page_window is not None:
            self.page_window.destroy()

    def update_time(self):
        con = sqlite3.connect(database=r"Billing_System.db")
        cur = con.cursor()
        self.current_time = time.strftime('%H:%M:%S') 
        self.tittlt2.config(text=f"Welcome to Inventory Management System \t\t\t   Date {str(time.strftime('%d/%m/%y'))}  \t\t\t  Time {str(self.current_time)}")
        total_sales = len(os.listdir('Bills'))
        self.Total_sales_lbl.config(text=f"Total Sales\n[{total_sales}]")
        cur.execute("select * from Employee")
        rows = cur.fetchall()
        self.Total_Emp_lbl.config(text=f"Total Employee\n[{str(len(rows))}]")
        cur.execute("select * from product")
        total_product = cur.fetchall()
        self.Totoal_ptoduct.config(text=f"Total Products\n[{str(len(total_product))}]")
        cur.execute("select * from Suplier")
        total_suplier = cur.fetchall()


        
        self.Total_suplier.config(text=f"Total supliers\n[{str(len(total_suplier))}]")
        cur.execute("select * from category")
        Total_Category = cur.fetchall()
        self.Total_Categories.config(text=f"Total Categories\n[{str(len(Total_Category))}]")
        self.tittlt2.after(1000,self.update_time)
    def close_all_windows(self, current_window):
        for window in [self.page1_window,self.page2_window,self.page3_window,self.page4_window,self.page5_window,self.page6_window]:
            if window and window != current_window:
                window.destroy()
    def employee2(self):
        if self.page1_window is not None:
            self.page1_window.destroy()
            time.sleep(1) 
        self.close_all_windows(self.page1_window)
        self.newwindow = Toplevel(self.root)
        self.new_obj = page2(self.newwindow)
        self.page1_window = self.newwindow
        self.page_window = self.newwindow
        
    def category(self):
        if self.page2_window is not None:
            self.page2_window.destroy()
            time.sleep(1)
        self.close_all_windows(self.page2_window)
        self.newwindow = Toplevel(self.root)
        self.new_obj = Categorie(self.newwindow)
        self.page2_window = self.newwindow
        self.page_window = self.newwindow
        
    def Sales(self):
        if self.page3_window is not None:
            self.page3_window.destroy()
            time.sleep(1)
        self.close_all_windows(self.page3_window)
        self.newwindow = Toplevel(self.root)
        self.new_obj = Sales(self.newwindow)
        self.page3_window = self.newwindow
        self.page_window = self.newwindow
        
    def Suplier(self):
        if self.page4_window is not None:
            self.page4_window.destroy()
            time.sleep(1)
        self.close_all_windows(self.page4_window)
        self.newwindow = Toplevel(self.root)
        self.new_obj = SupplyreClass(self.newwindow)
        self.page4_window = self.newwindow
        self.page_window = self.newwindow
        
    def product(self):
        if self.page5_window is not None:
            self.page5_window.destroy()
            time.sleep(1)
        self.close_all_windows(self.page5_window)
        self.newwindow = Toplevel(self.root)
        self.new_obj = product(self.newwindow)
        self.page5_window = self.newwindow
        self.page_window = self.newwindow
        
    def Bill_Area(self):
        if self.page6_window is not None:
            self.page6_window.destroy()
            time.sleep(1)
        self.close_all_windows(self.page6_window)
        self.newwindow = Toplevel(self.root)
        self.new_obj = Billing_area(self.newwindow)
        self.page6_window = self.newwindow
        self.page_window = self.newwindow
        
if __name__=="__main__":
    root=Tk()
    obj = page1(root)
    root.mainloop()