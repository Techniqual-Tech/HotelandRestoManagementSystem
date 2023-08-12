from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import mysql.connector

class CustomerDetails:
    def __init__(self,window):
        self.window=window
        self.window.title("CustomerDetail's")
        self.window.geometry("1280x725+0+0")
        self.window.configure(bg="white")

        #variable dec
        self.searchBy=StringVar()
        self.searchEntry=StringVar()

        Headinglabel=Label(self.window,text="CustomerDetail's",font=("times new roman",19,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE,width=85)
        Headinglabel.place(x=0,y=0)

        RefreshButton=Button(self.window,text="Refresh",font=("times new roman",16,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE,width=16,command=self.CustomerDetail)
        RefreshButton.place(x=550,y=670)

        #searchBy=Label(self.window,text="SearchBy:-",font=("times new roman",21,"bold"),bd=2,bg="red",relief=RIDGE)
        #searchBy.place(x=0,y=40)

        #combo_search=ttk.Combobox(self.window,font=("times new roman",15,"bold"),width=18,state="readonly",textvariable=self.searchBy)
        #combo_search["value"]=("CustomerRef","CustomerName","CustomerMobile","IdNumber","InDateTime","OutDateTime")
        #combo_search.current(0)
        #combo_search.place(x=150,y=44)

        #searchE=Entry(self.window,font=("times new roman",15,"bold"),bg="#F7EFE9",width=66,textvariable=self.searchEntry)
        #searchE.place(x=365,y=45)

        #Search=Button(self.window,text="Search",font=("times new roman",13,"bold"),bg="black",fg="yellow",width=20,relief=RIDGE,command=self.Search)
        #Search.place(x=1050,y=42)


        #function calling
        self.CustomerDetail()

    def CustomerDetail(self,querys="select * from allocatedroomdetails "):
        tree=ttk.Treeview(self.window)
        tree["columns"]=("Cref","CName","Gender","Nationality","CMob","CEmail","IdType","IdNum","RelativeContact","Add","Pin","floorno","roomtype","roomno","roomcode","securitydep","remark","TimeIn","TimeOut")

        s=ttk.Style(self.window)
        s.theme_use("classic")
        s.configure(".",font=("Helvetica",11,"bold"))
        s.configure("Treeview.Heading",foreground="black",font=("Helvetica",10,"bold"))

        tree['show']='headings'

        tree.column("Cref",width=70,minwidth=70,anchor=tk.CENTER)
        tree.column("CName",width=150,minwidth=150,anchor=tk.CENTER)
        tree.column("Gender",width=115,minwidth=115,anchor=tk.CENTER)
        tree.column("Nationality",width=130,minwidth=130,anchor=tk.CENTER)
        tree.column("CMob",width=120,minwidth=120,anchor=tk.CENTER)
        tree.column("CEmail",width=130,minwidth=130,anchor=tk.CENTER)
        tree.column("IdType",width=70,minwidth=70,anchor=tk.CENTER)
        tree.column("IdNum",width=200,minwidth=200,anchor=tk.CENTER)
        tree.column("RelativeContact",width=200,minwidth=200,anchor=tk.CENTER)
        tree.column("Add",width=70,minwidth=70,anchor=tk.CENTER)
        tree.column("Pin",width=150,minwidth=150,anchor=tk.CENTER)
        tree.column("floorno",width=115,minwidth=115,anchor=tk.CENTER)
        tree.column("roomtype",width=130,minwidth=130,anchor=tk.CENTER)
        tree.column("roomno",width=120,minwidth=120,anchor=tk.CENTER)
        tree.column("roomcode",width=130,minwidth=130,anchor=tk.CENTER)
        tree.column("securitydep",width=70,minwidth=70,anchor=tk.CENTER)
        tree.column("remark",width=70,minwidth=70,anchor=tk.CENTER)
        tree.column("TimeIn",width=200,minwidth=200,anchor=tk.CENTER)
        tree.column("TimeOut",width=200,minwidth=200,anchor=tk.CENTER)

        tree.heading("Cref",text="Cust_Ref",anchor=tk.CENTER)
        tree.heading("CName",text="Name",anchor=tk.CENTER)
        tree.heading("Gender",text="Gender",anchor=tk.CENTER)
        tree.heading("Nationality",text="Nationality",anchor=tk.CENTER)
        tree.heading("CMob",text="Mobile",anchor=tk.CENTER)
        tree.heading("CEmail",text="Email",anchor=tk.CENTER)
        tree.heading("IdType",text="IDType",anchor=tk.CENTER)
        tree.heading("IdNum",text="IDNumber",anchor=tk.CENTER)
        tree.heading("RelativeContact",text="RelativeContact",anchor=tk.CENTER)
        tree.heading("Add",text="Address",anchor=tk.CENTER)
        tree.heading("Pin",text="Pin",anchor=tk.CENTER)
        tree.heading("floorno",text="FloorNo",anchor=tk.CENTER)
        tree.heading("roomtype",text="RoomType",anchor=tk.CENTER)
        tree.heading("roomno",text="RoomNo",anchor=tk.CENTER)
        tree.heading("roomcode",text="RoomCode",anchor=tk.CENTER)
        tree.heading("securitydep",text="SecurityDeptosit",anchor=tk.CENTER)
        tree.heading("remark",text="Remark",anchor=tk.CENTER)
        tree.heading("TimeIn",text="TimeIn",anchor=tk.CENTER)
        tree.heading("TimeOut",text="TimeOut",anchor=tk.CENTER)

        scroll_x=Scrollbar(tree,orient=HORIZONTAL)
        scroll_y=Scrollbar(tree,orient=VERTICAL)
        scroll_x.pack(side=BOTTOM,fill='x')
        scroll_y.pack(side=RIGHT,fill='y')
        
        
        conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="hotelandrestoproject")
        my_cursor=conn.cursor()
        #query="select * from customerhistory "
        query=querys
        my_cursor.execute(query)
        
        i=0
        for ro in my_cursor:
            tree.insert('',i+1,text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11],ro[12],ro[13],ro[14],ro[15],ro[16],ro[17],ro[18]))
            i=i+1

        tree.place(x=0,y=40,width=1280,height=620)
        tree.config(xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.config(command=tree.xview)
        scroll_y.config(command=tree.yview)
    """def Search(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="vicky@123//",database="hotelandrestoproject")
        my_cursor=conn.cursor()
        mode=self.searchBy.get()
        value=self.searchEntry.get()
        #print(mode,value)
        if mode=="InDateTime" or mode=="OutDateTime":
            value=value+"%"
            print(value)
        querys="select * from customerhistory where {} LIKE '{}'".format(mode,value)
        my_cursor.execute(querys)
        for i in my_cursor:
            print(i)
        self.CustomerHistory(querys)"""
        
        

        



if __name__=="__main__":
    window=Tk()
    obj=CustomerDetails(window)
    window.mainloop()
