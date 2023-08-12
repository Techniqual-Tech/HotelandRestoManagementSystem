from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import mysql.connector

class FoodBillRecord:
    def __init__(self,window):
        self.window=window
        self.window.title("BillRecord's")
        self.window.geometry("1280x725+0+0")
        self.window.configure(bg="white")

        #variable dec
        self.searchBy=StringVar()
        self.searchEntry=StringVar()

        Headinglabel=Label(self.window,text="BillRecord's",font=("times new roman",19,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE,width=85)
        Headinglabel.place(x=0,y=0)

        RefreshButton=Button(self.window,text="Refresh",font=("times new roman",16,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE,width=16,command=self.BillHistory)
        RefreshButton.place(x=550,y=670)

        searchBy=Label(self.window,text="SearchBy:-",font=("times new roman",21,"bold"),bd=2,bg="red",relief=RIDGE)
        searchBy.place(x=0,y=40)

        combo_search=ttk.Combobox(self.window,font=("times new roman",15,"bold"),width=18,state="readonly",textvariable=self.searchBy)
        combo_search["value"]=("bill","datetime")
        combo_search.current(0)
        combo_search.place(x=150,y=44)

        searchE=Entry(self.window,font=("times new roman",15,"bold"),bg="#F7EFE9",width=66,textvariable=self.searchEntry)
        searchE.place(x=365,y=45)

        Search=Button(self.window,text="Search",font=("times new roman",13,"bold"),bg="black",fg="yellow",width=20,relief=RIDGE,command=self.Search)
        Search.place(x=1050,y=42)


        #function calling
        self.BillHistory()

    def BillHistory(self,querys="select * from billrecord "):
        tree=ttk.Treeview(self.window)
        tree["columns"]=("Sr_No","Bill","Amount","DateTime")

        s=ttk.Style(self.window)
        s.theme_use("classic")
        s.configure(".",font=("Helvetica",11,"bold"))
        s.configure("Treeview.Heading",foreground="black",font=("Helvetica",10,"bold"))

        tree['show']='headings'

        tree.column("Sr_No",width=70,minwidth=70,anchor=tk.CENTER)
        tree.column("Bill",width=150,minwidth=150,anchor=tk.CENTER)
        tree.column("Amount",width=115,minwidth=115,anchor=tk.CENTER)
        tree.column("DateTime",width=130,minwidth=130,anchor=tk.CENTER)

        tree.heading("Sr_No",text="Sr_No.",anchor=tk.CENTER)
        tree.heading("Bill",text="Bill",anchor=tk.CENTER)
        tree.heading("Amount",text="Amount",anchor=tk.CENTER)
        tree.heading("DateTime",text="DateTime",anchor=tk.CENTER)
        
        
        conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="hotelandrestoproject")
        my_cursor=conn.cursor()
        #query="select * from customerhistory "
        query=querys
        my_cursor.execute(query)
        
        i=0
        for ro in my_cursor:
            tree.insert('',i+1,text="",values=(ro[0],ro[1],ro[2],ro[3]))
            i=i+1

        tree.place(x=0,y=78,width=1280,height=580)

        self.Clear()

    def Search(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="vicky@123//",database="hotelandrestoproject")
        my_cursor=conn.cursor()
        mode=self.searchBy.get()
        value=self.searchEntry.get()
        #print(mode,value)
        if mode=="datetime":
            value=value+"%"
            print(value)
        querys="select * from billrecord where {} LIKE '{}'".format(mode,value)
        my_cursor.execute(querys)
        for i in my_cursor:
            print(i)
        self.BillHistory(querys)

    def Clear(self):
        self.searchEntry.set("")
        
        

        



if __name__=="__main__":
    window=Tk()
    obj=FoodBillRecord(window)
    window.mainloop()
