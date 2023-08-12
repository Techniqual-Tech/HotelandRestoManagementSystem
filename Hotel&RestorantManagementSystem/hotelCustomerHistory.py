from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import mysql.connector

class CustomerHistory:
    def __init__(self,window):
        self.window=window
        self.window.title("CustomerHistory")
        self.window.geometry("1280x725+0+0")
        self.window.configure(bg="white")

        #variable dec
        self.searchBy=StringVar()
        self.searchEntry=StringVar()

        Headinglabel=Label(self.window,text="CustomerHistory",font=("times new roman",19,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE,width=85)
        Headinglabel.place(x=0,y=0)

        RefreshButton=Button(self.window,text="Refresh",font=("times new roman",16,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE,width=16,command=self.CustomerHistory)
        RefreshButton.place(x=550,y=670)

        searchBy=Label(self.window,text="SearchBy:-",font=("times new roman",21,"bold"),bd=2,bg="red",relief=RIDGE)
        searchBy.place(x=0,y=40)

        combo_search=ttk.Combobox(self.window,font=("times new roman",15,"bold"),width=18,state="readonly",textvariable=self.searchBy)
        combo_search["value"]=("CustomerRef","CustomerName","CustomerMobile","IdNumber","InDateTime","OutDateTime")
        combo_search.current(0)
        combo_search.place(x=150,y=44)

        searchE=Entry(self.window,font=("times new roman",15,"bold"),bg="#F7EFE9",width=66,textvariable=self.searchEntry)
        searchE.place(x=365,y=45)

        Search=Button(self.window,text="Search",font=("times new roman",13,"bold"),bg="black",fg="yellow",width=20,relief=RIDGE,command=self.Search)
        Search.place(x=1050,y=42)


        #function calling
        self.CustomerHistory()

    def CustomerHistory(self,querys="select * from customerhistory "):
        tree=ttk.Treeview(self.window)
        tree["columns"]=("Cref","CName","CMob","AddPin","IdType","IdNum","RoomCod","TimeIn","TimeOut")

        s=ttk.Style(self.window)
        s.theme_use("classic")
        s.configure(".",font=("Helvetica",11,"bold"))
        s.configure("Treeview.Heading",foreground="black",font=("Helvetica",10,"bold"))

        tree['show']='headings'

        tree.column("Cref",width=70,minwidth=70,anchor=tk.CENTER)
        tree.column("CName",width=150,minwidth=150,anchor=tk.CENTER)
        tree.column("CMob",width=115,minwidth=115,anchor=tk.CENTER)
        tree.column("AddPin",width=130,minwidth=130,anchor=tk.CENTER)
        tree.column("IdType",width=120,minwidth=120,anchor=tk.CENTER)
        tree.column("IdNum",width=130,minwidth=130,anchor=tk.CENTER)
        tree.column("RoomCod",width=70,minwidth=70,anchor=tk.CENTER)
        tree.column("TimeIn",width=200,minwidth=200,anchor=tk.CENTER)
        tree.column("TimeOut",width=200,minwidth=200,anchor=tk.CENTER)

        tree.heading("Cref",text="Cust_Ref",anchor=tk.CENTER)
        tree.heading("CName",text="Name",anchor=tk.CENTER)
        tree.heading("CMob",text="Mobile",anchor=tk.CENTER)
        tree.heading("AddPin",text="Address",anchor=tk.CENTER)
        tree.heading("IdType",text="ID Type",anchor=tk.CENTER)
        tree.heading("IdNum",text="ID Number",anchor=tk.CENTER)
        tree.heading("RoomCod",text="RoomCode",anchor=tk.CENTER)
        tree.heading("TimeIn",text="In Time",anchor=tk.CENTER)
        tree.heading("TimeOut",text="Out Time",anchor=tk.CENTER)
        
        
        conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="hotelandrestoproject")
        my_cursor=conn.cursor()
        #query="select * from customerhistory "
        query=querys
        my_cursor.execute(query)
        
        i=0
        for ro in my_cursor:
            tree.insert('',i+1,text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8]))
            i=i+1

        tree.place(x=0,y=78,width=1280,height=580)

    def Search(self):
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
        self.CustomerHistory(querys)
        
        

        



if __name__=="__main__":
    window=Tk()
    obj=CustomerHistory(window)
    window.mainloop()
